#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os
import logging
from http.cookies import SimpleCookie
class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        s = self.path
        cookies = SimpleCookie(self.headers.get('Cookie'))
        print(str(cookies))
        print(self.headers)
        log = logging.getLogger("my-logger")
        log.info(cookies)
        log.info(self.headers)
        #self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'https://vercel-jwt-github-action.vercel.app')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
        self.send_header('Access-Control-Allow-Headers','*')
        self.send_header('Content-type', 'application/json')
        self.send_response(200)
        self.end_headers()
        myenv = os.getenv('MYENV')
        message = {"a": "b" }
        self.wfile.write(bytes("{\"result\": 200}", "utf-8"))
        return
