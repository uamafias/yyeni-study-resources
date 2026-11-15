// Local-only PDF OCR using Apple's installed PDFKit/Vision. Originals are never modified.
// Usage: swift pdf_ocr_macos.swift INPUT OUTPUT_DIRECTORY [FIRST_PAGE] [LAST_PAGE]
// Page records are leads: mathematical notation must be checked against the image.
import Foundation
import PDFKit
import Vision
import AppKit
import CryptoKit

let args = CommandLine.arguments
guard args.count >= 3 else { fatalError("Expected INPUT OUTPUT_DIRECTORY [FIRST_PAGE] [LAST_PAGE]") }
let input = URL(fileURLWithPath: args[1]).standardizedFileURL
let output = URL(fileURLWithPath: args[2]).standardizedFileURL
let bytes = try Data(contentsOf: input, options: .mappedIfSafe)
let hash = SHA256.hash(data: bytes).map { String(format: "%02x", $0) }.joined()
guard let document = PDFDocument(url: input) else { fatalError("Unreadable PDF") }
let first = args.count > 3 ? Int(args[3])! : 1
let last = args.count > 4 ? Int(args[4])! : document.pageCount
guard first > 0 && last >= first && last <= document.pageCount else { fatalError("Invalid page range") }
try FileManager.default.createDirectory(at: output, withIntermediateDirectories: true)
let encoder = JSONSerialization.WritingOptions([.prettyPrinted, .sortedKeys])
let metadata: [String:Any] = ["source":input.path,"source_sha256":hash,"pages":document.pageCount,
    "engine":"Apple Vision VNRecognizeTextRequest accurate, en-GB, no language correction",
    "revision":VNRecognizeTextRequest.currentRevision,"max_pixel_dimension":2200,
    "purpose":"Internal source-discovery derivative; not verified mathematical transcription"]
let metaURL = output.appendingPathComponent("metadata.json")
if FileManager.default.fileExists(atPath: metaURL.path) {
    let old = try JSONSerialization.jsonObject(with: Data(contentsOf: metaURL)) as! [String:Any]
    guard old["source_sha256"] as? String == hash else { fatalError("Existing OCR belongs to different bytes") }
    guard old["engine"] as? String == metadata["engine"] as? String,
          old["revision"] as? Int == metadata["revision"] as? Int,
          old["max_pixel_dimension"] as? Int == metadata["max_pixel_dimension"] as? Int else {
        fatalError("OCR settings changed; use a new derivative directory")
    }
}
try JSONSerialization.data(withJSONObject:metadata,options:encoder).write(to:metaURL,options:.atomic)
for number in first...last {
    try autoreleasepool {
        let destination = output.appendingPathComponent(String(format:"page-%04d.json",number))
        if FileManager.default.fileExists(atPath:destination.path) { return }
        guard let page = document.page(at:number-1) else { fatalError("Missing page") }
        let bounds = page.bounds(for:.mediaBox)
        let scale = 2200.0 / max(bounds.width,bounds.height)
        let width = Int(ceil(bounds.width*scale)), height = Int(ceil(bounds.height*scale))
        guard let context = CGContext(data:nil,width:width,height:height,bitsPerComponent:8,
            bytesPerRow:0,space:CGColorSpaceCreateDeviceRGB(),bitmapInfo:CGImageAlphaInfo.premultipliedLast.rawValue) else { fatalError("Render failed") }
        context.setFillColor(CGColor.white); context.fill(CGRect(x:0,y:0,width:width,height:height))
        context.scaleBy(x:scale,y:scale); context.translateBy(x:-bounds.minX,y:-bounds.minY)
        page.draw(with:.mediaBox,to:context)
        guard let image = context.makeImage() else { fatalError("Image failed") }
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.recognitionLanguages = ["en-GB"]
        request.usesLanguageCorrection = false
        try VNImageRequestHandler(cgImage:image).perform([request])
        let lines:[[String:Any]] = (request.results ?? []).compactMap { observation in
            guard let candidate = observation.topCandidates(1).first else { return nil }
            let b = observation.boundingBox
            return ["text":candidate.string,"confidence":candidate.confidence,
                    "box":[b.minX,b.minY,b.width,b.height]]
        }
        let record:[String:Any] = ["pdf_page":number,"source_sha256":hash,"lines":lines]
        try JSONSerialization.data(withJSONObject:record,options:encoder).write(to:destination,options:.atomic)
        if number == first || number % 25 == 0 || number == last { print("OCR page \(number)/\(last)"); fflush(stdout) }
    }
}
