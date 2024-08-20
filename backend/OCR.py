from nanonets import NANONETSOCR
import os
from dotenv import load_dotenv, dotenv_values 

model = NANONETSOCR()
load_dotenv()


model.set_token(os.getenv('API_KEY'))

def imgtotext(image_path):
    imgtotext_filename = "imgtotext_" + os.path.basename(image_path).split('.')[0] + ".txt"

    output_path = os.path.join(os.path.dirname(image_path), "image_output/", imgtotext_filename)
    model.convert_to_txt(image_path, formatting = 'none', output_file_name = output_path)

    return output_path
