import whisper

model = whisper.load_model("base")
result = model.transcribe("test_audio.mp3", fp16=False)

with open("transcribed_test_audio.txt", "w") as f:
    f.write(result['text'])
