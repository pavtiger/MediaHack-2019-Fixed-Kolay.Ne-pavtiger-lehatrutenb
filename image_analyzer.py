from PIL import Image
from pytesseract import image_to_string
import io
import os
from google.cloud import vision
from google.cloud.vision import types

def get_text_on_image(img):
	image = Image.open(img, mode='r')
	print(image_to_string(image, lang='rus'))

def get_image_tags(img):
	client = vision.ImageAnnotatorClient()

	file_name = os.path.join(
    	os.path.dirname(__file__),
    	img)

	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	response = client.label_detection(image=image)
	labels = response.label_annotations

	print('Labels:')
	for label in labels:
	    print(label.description)

get_text_on_image('some1.jpg')