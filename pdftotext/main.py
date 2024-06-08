from flask import Flask, request, send_file
from flask_cors import CORS
import os
from imgtotxt import imgtotxt

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/imgtotxt', methods=['POST'])
def imgtotxtfunc():
    print(request.files)
    if 'file' not in request.files:
        return 'No file part',400
    file = request.files['files']
    if file.filename == '':
        return 'No selected file',400
    
    imagepath = os.path.join(file.filename)
    file.save(imagepath)

    textpath = imgtotxt(imagepath)
    return send_file(textpath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")