import http.server
import socketserver

PORT = 8000
command_string = """<|>RUN<|>cmd /c echo BOOM > c:\\data\\oooooook<|>\r\n\r\n<|>RUN<|>cmd /c echo BOOM > c:\\data\\RENNNN<|>"""

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/command':
            # Inviare la risposta al client
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(command_string.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
