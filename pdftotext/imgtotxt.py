from nanonets import NANONETSOCR
import os
model = NANONETSOCR()


model.set_token('0bd728c2-2506-11ef-b795-d6d3c2ad6cc3')

def imgtotxt(imagepath):
    model.convert_to_txt(imagepath, formatting='none', output_file_name='output.txt')
    output_path = os.path.join(os.path.dirname('output.txt'))
    return output_path




