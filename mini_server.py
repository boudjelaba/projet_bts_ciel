# BONUS – Mini serveur HTTP
# TODO : simple serveur HTTP pour afficher "Hello World"

from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 8000
server_address = ("", port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Serveur démarré sur le port {port}")
httpd.serve_forever()
