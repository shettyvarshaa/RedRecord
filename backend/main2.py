from flask import Flask, request, send_file
from flask_cors import CORS
import os
from Transcriber import transcribe_audio_file
from OCR import imgtotext

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Welcome to Cerebro 😎'

@app.route('/transcribe', methods = ['POST'])
def transcribe_audio():
    print(request.files)
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    audio_path = os.path.join("audio/", file.filename)
    file.save(audio_path)
    
    transcription_path = transcribe_audio_file(audio_path)
    
    return send_file(transcription_path, as_attachment=True)

@app.route('/imgtotext', methods = ['POST'])
def image_to_text():
    print(request.files)
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    image_path = os.path.join("images/", file.filename)
    file.save(image_path)

    text_path = imgtotext(image_path)

    return send_file(text_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
