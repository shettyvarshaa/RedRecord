from flask import Flask, request, send_file
import os
from transcriber import transcribe_audio_file
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    print(request.files)
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    audio_path = os.path.join(  file.filename)
    file.save(audio_path)
    
    transcription_path = transcribe_audio_file(audio_path)
    
    return send_file(transcription_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")