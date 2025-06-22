from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Halo dari Flask di Vercel!")

# Wajib untuk serverless
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
