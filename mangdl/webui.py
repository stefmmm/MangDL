from http.server import BaseHTTPRequestHandler, HTTPServer
from mangdl.version import __version__
ver = __version__

hostName = "localhost"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head></head>", "utf-8"))
        self.wfile.write(bytes("<title>Hyaku TEST</title>", "utf-8"))
        self.wfile.write(bytes("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/css/uikit.min.css'/>", "utf-8"))
        self.wfile.write(bytes("<script src='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/js/uikit.min.js'></script>", "utf-8"))
        self.wfile.write(bytes("<script src='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/js/uikit-icons.min.js'></script>", "utf-8"))
        self.wfile.write(bytes("</head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-container uk-margin-large-top'>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-card uk-card-body uk-card-primary'>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-card-badge uk-label''>WIP</div>", "utf-8"))
        self.wfile.write(bytes("<h3 class='uk-card-title'>MangDL</h3>", "utf-8"))
        self.wfile.write(bytes(f"<p>Version: {ver}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")