from nanonets import NANONETSOCR
import os
from dotenv import load_dotenv

model = NANONETSOCR()
load_dotenv()

model.set_token(os.getenv('API_KEY'))

def image_to_text(image_path):
    imgtotext_filename = "ocr_" + os.path.basename(image_path).split('.')[0] + ".txt"

    output_path = os.path.join(os.path.dirname(image_path), "image_output/", imgtotext_filename)
    model.convert_to_txt(image_path, formatting = 'none', output_file_name = output_path)

    with open(output_path, 'r') as file:
        outputText = file.read()

    return outputText