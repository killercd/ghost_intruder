import http.server
import socketserver
import logging
import os
PORT = 80

bodyc= b"""<html></html>"""

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):


    def log_client_request(self, content=""):
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        logging.info(f"Client IP: {client_ip}, User-Agent: {user_agent}\nContent: {content}")
        with open('client_info.txt', 'a') as file:
            file.write(f"\n----------------------\nClient IP: {client_ip}, User-Agent: {user_agent}\nContent: {content}\n----------------------\n")

    def redirect(self):
        self.send_response(302)
        self.send_header("Location", "http://www.google.com")
        self.end_headers()

    def okresp(self):
        self.server_version="Apache 1.0"
        self.sys_version = ''
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=ISO-8859-1")
        self.end_headers()
        self.wfile.write(bodyc)

    def do_GET(self):
        if self.path == '/cutedino.jpg':
            filename="cutedino.jpg"
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.send_header("Content-Length", str(os.path.getsize(filename)))
            self.end_headers()
            with open(filename, 'rb') as file:
                self.wfile.write(file.read())

        self.log_client_request(content=self.path)
        #self.redirect()
        self.okresp()

    def do_POST(self):
        import pdb; pdb.set_trace()
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        self.log_client_request(content=post_data)
        #self.redirect()
        self.okresp()
        
    def do_PUT(self):
        self.log_client_request()
        self.redirect()

    def do_DELETE(self):
        self.log_client_request()
        self.redirect()

    def do_HEAD(self):
        self.log_client_request()
        self.redirect()

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    logging.basicConfig(level=logging.INFO, filename='server.log', 
                        format='%(asctime)s - %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S')
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
