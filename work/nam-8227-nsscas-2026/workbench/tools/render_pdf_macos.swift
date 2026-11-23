// Local source renderer, PDFKit. Input PDF is opened read-only.
// Usage: swift render_pdf_macos.swift INPUT OUTPUT_DIRECTORY PAGE [PAGE ...]
import Foundation
import PDFKit
import AppKit
let args = CommandLine.arguments
guard args.count >= 4, let doc = PDFDocument(url: URL(fileURLWithPath:args[1])) else { fatalError("INPUT OUTPUT PAGE...") }
let out = URL(fileURLWithPath:args[2])
try FileManager.default.createDirectory(at:out, withIntermediateDirectories:true)
for token in args.dropFirst(3) {
    let n = Int(token)!
    guard let p = doc.page(at:n-1) else { fatalError("Missing page") }
    let b = p.bounds(for:.mediaBox), scale = 2.0
    let rotated = abs(p.rotation) % 180 != 0
    let width = rotated ? b.height : b.width, height = rotated ? b.width : b.height
    let w = Int(ceil(width*scale)), h = Int(ceil(height*scale))
    let c = CGContext(data:nil,width:w,height:h,bitsPerComponent:8,bytesPerRow:0,
        space:CGColorSpaceCreateDeviceRGB(),bitmapInfo:CGImageAlphaInfo.premultipliedLast.rawValue)!
    c.setFillColor(CGColor.white); c.fill(CGRect(x:0,y:0,width:w,height:h))
    c.scaleBy(x:scale,y:scale)
    if rotated, let ref = p.pageRef {
        c.concatenate(ref.getDrawingTransform(.mediaBox, rect:CGRect(x:0,y:0,width:width,height:height), rotate:0, preserveAspectRatio:true))
        c.drawPDFPage(ref)
    } else {
        c.translateBy(x:-b.minX,y:-b.minY)
        p.draw(with:.mediaBox,to:c)
    }
    let rep = NSBitmapImageRep(cgImage:c.makeImage()!)
    try rep.representation(using:.png,properties:[:])!.write(to:out.appendingPathComponent(String(format:"page-%04d.png",n)))
}
