#!/usr/bin/env python3
import http.server
import socketserver
import os
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import re

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        path = urlparse(self.path)
        query_components = parse_qs(urlparse(self.path).query)
        
        if path.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()

            word_param = query_components.get('str', None)
            
            if word_param:
                word = word_param[0]

                result = {}
                lower = 0
                upper = 0
                digits = 0
                specials = 0

                specials_regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

                for char in word:
                    if char.isalpha():
                        if char.islower():
                            lower += 1
                        else:
                            upper += 1
                    elif char.isdigit():
                        digits += 1
                    elif re.search(specials_regex, char):
                        specials += 1
                    
                    
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
