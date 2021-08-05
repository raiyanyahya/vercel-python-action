#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        self.send_response(200)
        print(self.headers)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        myenv = os.getenv('MYENV')
        message = 'Hello, stranger!' + myenv
        self.wfile.write(message.encode())
        return
