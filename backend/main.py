from fastapi import FastAPI
import gemini
from datamodels import Session, PreviousContent
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/randomQuestion")
async def randomQuestion(contents: PreviousContent):
    return {"question": gemini.generateRandomQuestion(contents.contentList)}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/")
async def root():
    return {"message": "Welcome to the server of ARC-AI"}