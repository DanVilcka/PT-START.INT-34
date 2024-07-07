from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthzHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'200 OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HealthzHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()