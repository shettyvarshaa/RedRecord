from nanonets import NANONETSOCR
import os
model = NANONETSOCR()


model.set_token('0bd728c2-2506-11ef-b795-d6d3c2ad6cc3')

def imgtotext(image_path):
    imgtotext_filename = "imgtotext_" + os.path.basename(image_path).split('.')[0] + ".txt"

    output_path = os.path.join(os.path.dirname(image_path), "image_output/", imgtotext_filename)
    model.convert_to_txt(image_path, formatting = 'none', output_file_name = output_path)

    return output_path
