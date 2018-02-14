from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("localhost", 80)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
