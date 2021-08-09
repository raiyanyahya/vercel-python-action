#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler
import os
import jwt
from http.cookies import SimpleCookie

secret_key = os.getenv('SECRET')

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        c = SimpleCookie()
        print("self is",str(self))
        print("headers payload are ", self.headers.get_payload())
        
        print("secretkey is ", secret_key)
        c.load("\n".join(self.headers.get_all('cookie',failobj=[])))
        print("the cookie is", c)
        encoded_jwt = c["__Secure-next-auth.session-token"].value
        print("encoded secret is ", encoded_jwt)
        valid_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS512"])
        print(valid_jwt)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'https://vercel-jwt-github-action.vercel.app')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
        self.send_header('Access-Control-Allow-Headers','*')
        self.send_header('Content-type', 'application/json')
        
        self.end_headers()
        self.wfile.write(bytes("{\"result\": 200}", "utf-8"))
        return
