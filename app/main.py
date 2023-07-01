from flask import Flask, request, jsonify, send_file, Response
import base64

# Set up the Flask app
app = Flask(__name__)

# Define the API endpoint for the plugin logo
@app.route('/logo.png', methods=['GET'])
def plugin_logo():
    filename = 'images/logo.png'
    return send_file(filename, mimetype='image/png')


# Define the API endpoint for the plugin manifest
@app.route('/ai-plugin.json', methods=['GET'])
def plugin_manifest():
    host = request.headers['Host']
    with open('./ai-plugin.json') as f:
        text = f.read()
        return Response(text, mimetype='text/json')


# Define the API endpoint for the OpenAPI specification
@app.route('/openapi.yaml', methods=['GET'])
def openapi_spec():
    host = request.headers['Host']
    with open('./openapi.yaml') as f:
        text = f.read()
        return Response(text, mimetype='text/yaml')

@app.route('/test', methods=['GET'])
def test():
    return "Hello World"

if __name__ == '__main__':
    # Set debug=True to enable auto-reloading when you make changes to the code
    app.run(debug=True, host='127.0.0.1', port=5000)
