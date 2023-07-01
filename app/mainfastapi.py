from flask import Flask, request, jsonify, send_file, Response
import base64

# Set up the Flask app
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/logo.png')
def plugin_logo():
    filename = 'images/logo.png'
    return send_file(filename, mimetype='image/png')

@app.get('/ai-plugin.json')
def plugin_manifest():
    host = request.headers['Host']
    with open('./ai-plugin.json') as f:
        text = f.read()
        return Response(text, mimetype='text/json')

@app.get('/openapi.yaml')
def openapi_spec():
    host = request.headers['Host']
    with open('./openapi.yaml') as f:
        text = f.read()
        return Response(text, mimetype='text/yaml')
