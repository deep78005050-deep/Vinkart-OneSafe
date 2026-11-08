import http.server
import socketserver
import os

PORT = 8080
Directory = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=Directory, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Vinkart OneSafe Server running at: http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
