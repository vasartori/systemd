import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerHttp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            env_var = "Valor da variavel de sistema TESTE: {}".format(os.environ['TESTE'])
        except KeyError:
            env_var = ""
        mensagem = "Oi, respondendo na porta: {}. {}".format(PORT, env_var)
        self.wfile.write(str.encode(mensagem))
        return


def run():
    server = HTTPServer(('', PORT), ServerHttp)
    print("Servidor iniciado na porta: {}".format(PORT))
    server.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        PORT = int(sys.argv[1])
        run()
    else:
        PORT = 8000
        run()
