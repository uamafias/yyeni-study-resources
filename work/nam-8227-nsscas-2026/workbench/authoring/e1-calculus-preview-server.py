"""Local static derivative render; only the proof page and installed KaTeX assets."""
from http.server import BaseHTTPRequestHandler,HTTPServer
from pathlib import Path
import mimetypes,re,sys
A=Path(__file__).resolve().parent
K=Path(sys.argv[1]).resolve()/'node_modules/katex/dist'
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path in ('/','/e1-calculus-render.html'):p=A/'e1-calculus-render.html'
  elif self.path=='/katex.min.css':p=K/'katex.min.css'
  elif re.fullmatch(r'/fonts/KaTeX_[A-Za-z0-9_-]+\.(?:woff2?|ttf)',self.path):p=K/self.path.lstrip('/')
  else:self.send_error(404);return
  if not p.is_file():self.send_error(404);return
  self.send_response(200);self.send_header('Content-Type',mimetypes.guess_type(p.name)[0]or'application/octet-stream');self.end_headers();self.wfile.write(p.read_bytes())
 def log_message(self,*args):pass
HTTPServer(('127.0.0.1',8769),Handler).serve_forever()
