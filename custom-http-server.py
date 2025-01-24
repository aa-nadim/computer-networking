import logging
from http.server import HTTPServer, SimpleHTTPRequestHandler

class LoggingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"GET request for {self.path}")
        super().do_GET()

# Configure logging
logging.basicConfig(level=logging.INFO)
PORT = 8000

# Start the server
httpd = HTTPServer(("localhost", PORT), LoggingHandler)
print(f"Serving HTTP on port {PORT}")
httpd.serve_forever()
