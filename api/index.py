#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os
import logging
from http.cookies import SimpleCookie
class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        s = self.path
        self.send_response(200)
        cookies = SimpleCookie(self.headers.get('Cookie'))
        print(str(cookies))
        log = logging.getLogger("my-logger")
        log.info(cookies)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'https://vercel-jwt-github-action.vercel.app')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
        self.send_header('Access-Control-Allow-Headers','X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        myenv = os.getenv('MYENV')
        message = {"Hello, stranger!": myenv }
        self.wfile.write(message)
        return
