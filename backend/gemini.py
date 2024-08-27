import json

from dotenv import load_dotenv
import os
from urllib import request

load_dotenv()

URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"


def generateCall(prompt):
    endpoint = URL + "?key=" + os.getenv('GEMINI_KEY')
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = json.dumps({
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }).encode()
    req = request.Request(endpoint, data, headers)
    response = request.urlopen(req)
    return json.loads(response.read())['candidates'][0]['content']['parts'][0]['text']


SUMMARY_FILTER = ("Generate a report on the following lecture content along with three features. The first feature is to generate a summary of the given content in bullet points and detailed. not a single point should be missed. A complete notes. The second feature is the reference section which includes minimum 3 links papers and 3 links blog posts or articles and 1 textbook. Third feature is one youtube link which is relevant to the conntent given.\nContent:\n")

RANDOM_FILTER = "Generate a random a question based on one of these content:\n"

def generateSummary(content):
    return generateCall(SUMMARY_FILTER + content)


def generateRandomQuestion(contents):
    sentence = ""
    for i in range(len(contents)):
        append = "content"+str(i+1)+": "+contents[i]+"\n"
        sentence += append
    prompt = RANDOM_FILTER+sentence
    return generateCall(prompt)
