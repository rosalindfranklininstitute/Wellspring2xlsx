from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from wellspring2xlsx import ws2xlsx

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/data/<path:path>')
def send_js(path):
    return send_from_directory('/tmp/', path)

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('/tmp/uploaded.csv')
    ws2xlsx('/tmp/uploaded.csv', '/tmp/uploaded.xlsx')
    return redirect(url_for('download'))
