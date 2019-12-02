#!/usr/bin/env python3
from http.server import HTTPServer,CGIHTTPRequestHandler
server_address = ("", 5000)
CGIHTTPRequestHandler.cgi_directories = ["/cgi"]

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()


