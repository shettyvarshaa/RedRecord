import whisper
import os

def transcribe_audio_file(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, fp16=False)

    transcription_filename = "transcribed_" + os.path.basename(audio_path).split('.')[0] + ".txt"
    transcription_path = os.path.join(os.path.dirname(audio_path), "audio_output/", transcription_filename)

    with open(transcription_path, "w") as file:
        file.write(result['text'])

    return result['text']
