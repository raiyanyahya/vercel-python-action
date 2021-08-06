#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os
import logging
from http.cookies import SimpleCookie
class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        s = self.path
        print("this is path ",s.headers.get('Cookie'))
        print("http cookie", SimpleCookie(os.environ["HTTP_COOKIE"]))

        cookies = SimpleCookie(self.headers.get('Cookie'))
        print("cookie",str(cookies))
        print("header",self.headers)
        print("value", cookies['__Secure-next-auth.session-token'].value)
        
        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'https://vercel-jwt-github-action.vercel.app')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
        self.send_header('Access-Control-Allow-Headers','*')
        self.send_header('Content-type', 'application/json')
        
        self.end_headers()
        myenv = os.getenv('MYENV')
        message = {"a": "b" }
        self.wfile.write(bytes("{\"result\": 200}", "utf-8"))
        return
