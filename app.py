from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"AEGIS Backend on port {port} is alive!\n".encode())


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
server = HTTPServer(("127.0.0.1", port), Handler)

print(f"Backend listening on port {port}")
server.serve_forever()
