from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import os

import gemini
from Transcriber import transcribe_audio_file
from OCR import image_to_text
from datamodels import Session, PreviousContent

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
async def generate(session: Session):
    return {"summary": gemini.generateSummary(session.transcript)}

@app.post("/transcribe")
async def transcribe(file: UploadFile):
    # print(file.)
    # if 'file' not in file:
    #     return 'No file part', 400
    # if file.filename == '':
    #     return 'No selected file', 400
    
    audio_path = os.path.join("audio/", file.filename)
    # file.save(audio_path)
    
    transcribedText = transcribe_audio_file(audio_path)
    return { "message": transcribedText }

@app.post("/ocr")
async def getText(file: UploadFile = File(...)):
    # print(file)
    # if 'file' not in file:
    #     return 'No file part', 400
    # if file.filename == '':
    #     return 'No selected file', 400
    
    image_path = os.path.join("images/", file.filename)
    print(image_path)
    with open(image_path, "wb") as imgFile:
        imgFile.write(file.file.read())
    # file.write(image_path)

    ocrText = image_to_text(image_path)

    return { "ocrText": ocrText }

@app.post("/randomQuestion")
async def randomQuestion(contents: PreviousContent):
    return {"question": gemini.generateRandomQuestion(contents.contentList)}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/")
async def root():
    return {"message": "Welcome to the server of ARC-AI"}