from PIL import Image
from pytesseract import image_to_string
import io
from google.cloud import vision
from google.cloud.vision import types
from text_analyzer import check_text

def annotate(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection

def report(annotations):
    ret = {}

    if annotations.web_entities:
        for entity in annotations.web_entities:
            ret[entity.description] = entity.score

    return ret

def get_text_on_image(img):
    image = Image.open(img, mode='r')
    
    return image_to_string(image, lang='eng')

def check_picture(img, tag):
    """ Takes image and tags.
    Returns: True if image have
    ratio with tags,
    False if not """

    text_on_image = get_text_on_image(img)
    if(check_text(text_on_image, tag)):
        return True
    web_entries = report(annotate(img))
    if(check_text(' '.join(web_entires))):
        return True
    return False

if __name__ == '__main__':
    img = 'tyan.jpg'

    text = get_text_on_image(img)
    web_entries = report(annotate(img))