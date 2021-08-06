#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os
import json
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
        self.send_header('Access-Control-Allow-Headers','*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        myenv = os.getenv('MYENV')
        message = {"a": "b" }
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
        return
