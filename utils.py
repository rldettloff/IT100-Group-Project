import typing
import os
from PIL import Image
from flask import url_for

def process_file(filename:str, subdir:str) -> dict:
    result = {}
    parts = filename[:-4].split('__')
    result['title'] = ' '.join(parts[0].split('_'))
    result['artist'] = ' '.join(parts[1].split('_'))
    result['url'] = url_for('static', filename=subdir+"/"+filename)
    return result

def save_picture(picture, title, author):
    picture_fn = title.replace(" ","_") + "__" + author.replace(" ","_")
    picture_path = os.path.join(os.path.dirname(__file__), 'static/submitted', picture_fn)
    i = Image.open(picture)
    i.save(picture_path+'.jpg', format='JPEG')

if __name__ == '__main__':
    example = 'Mona_Lisa__Da_Vinci.jpg'
    print(process_file(example, 'historical'))
