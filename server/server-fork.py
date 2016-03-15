from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import daemon


class ServerHttp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        mensagem = "Oi, respondendo na porta: {}".format(PORT)
        self.wfile.write(str.encode(mensagem))
        return


def run():
    server = HTTPServer(('', PORT), ServerHttp)
    server.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        PORT = int(sys.argv[1])
    else:
        PORT = 8000
    with daemon.DaemonContext():
        run()
