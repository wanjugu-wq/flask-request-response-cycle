#!/usr/bin/env python3

from flask import Flask,g,request,make_response,current_app
import os

app = Flask(__name__)
@app.route()
def get_request():
    g.path = os.path.abspath(os.getcwd())


@app.route("/")
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    respone_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    status_code = 200
    headers = {}
    return make_response(respone_body,status_code,headers)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
