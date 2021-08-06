#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os
import logging
from http.cookies import SimpleCookie
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        self.send_response(200)
        cookies = SimpleCookie(self.headers.get('Cookie'))
        print(str(cookies)
        log = logging.getLogger("my-logger")
        log.info(self.headers)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        myenv = os.getenv('MYENV')
        message = 'Hello, stranger!' + myenv
        self.wfile.write(message.encode())
        return
