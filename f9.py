import vk_api
import random
import numpy as np
import requests
from pprint import pprint
import urllib
from text_analyzer import check_text
from image_analyzer import get_image_tags

class f9:
    def __init__(self):
        n = 0
        n += 1
    def get_filtered_news(self, tokken, offset, count, tags):
        tr = True
        try:
            vk = vk_api.VkApi(token=tokken)
            m2 = vk.method('newsfeed.get', {'count':count + offset, 'filters':'post'})
            img_url = m2['items'][((count + offset) % 100) - 1]['attachments'][0]['photo']['sizes'][-1]['url']
            text = m2['items'][((count + offset) % 100) - 1]['text']
        except:
            vk = vk_api.VkApi(token=tokken)
            tr = False
            m2 = vk.method('newsfeed.get', {'count': count + offset, 'filters': 'post'})
            #pprint(m2['items'][((count + offset) % 100) - 1]['attachments'][0])
            return 'bad request'
        if(tr):
            check_text(text)
            get_image_tags(img_url)
    def public_posts(self, tokken, offset, count, tags, pub_id):
        tr = True
        try:
            vk = vk_api.VkApi(token=tokken)
            m2 = vk.method('newsfeed.get', {'count':count + offset, 'filters':'post', 'source_ids': '-'+str(pub_id)})
            img_url = m2['items'][((count + offset) % 100) - 1]['attachments'][0]['photo']['sizes'][-1]['url']
            text = m2['items'][((count + offset) % 100) - 1]['text']
        except:
            vk = vk_api.VkApi(token=tokken)
            tr = False
            m2 = vk.method('newsfeed.get', {'count': count + offset, 'filters': 'post'})
            #pprint(m2['items'][((count + offset) % 100) - 1]['attachments'][0])
            return 'bad request'
        if(tr):
            check_text(text)
            get_image_tags(img_url)
#gl = Bot()
#tokken = '35db77277a6e00ea8035db2316ed190de24ca77c162c958eb72e83f70cc765b9a4d48dab35662aebfd65a'
#gl.public_posts(tokken, 0, 1, ['fd', 'fg', 'tr'], 'tnull')
#for i in range(1, 80):
#print(gl.get_filtered_news(tokken, i, 1, ['fd', 'fg', 'tr']))
