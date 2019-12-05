#!/usr/bin/env python3
import configparser
config = configparser.ConfigParser()
config.read('invertor.ini')
port=int(config['DEFAULT']['server_port'])
from http.server import HTTPServer,CGIHTTPRequestHandler
server_address = ("", port)
CGIHTTPRequestHandler.cgi_directories = ["/cgi"]

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()


