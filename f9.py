import vk_api
import random
import numpy as np
import requests
from pprint import pprint

class Bot:
    def __init__(self):
        n = 0
        n += 1
    def get_filtered_news(self, tokken, offset, count, tags):
        try:
            vk = vk_api.VkApi(token=tokken)
            m2 = vk.method('newsfeed.get', {'count':count + offset, 'filters':'post'})
            img_url = m2['items'][((count + offset) % 100) - 1]['attachments'][0]['photo']['sizes'][-1]['url']
            text = m2['items'][((count + offset) % 100) - 1]['text']
        except:
            vk = vk_api.VkApi(token=tokken)
            m2 = vk.method('newsfeed.get', {'count': count + offset, 'filters': 'post'})
            #pprint(m2['items'][((count + offset) % 100) - 1]['attachments'][0])
            return 'bad request'
    def public_posts(self, tokken, offset, count, tags, pub_id):
        try:
            vk = vk_api.VkApi(token=tokken)
            m2 = vk.method('newsfeed.get', {'count':count + offset, 'filters':'post', 'source_ids': '-'+str(pub_id)})
            img_url = m2['items'][((count + offset) % 100) - 1]['attachments'][0]['photo']['sizes'][-1]['url']
            text = m2['items'][((count + offset) % 100) - 1]['text']
        except:
            vk = vk_api.VkApi(token=tokken)
            m2 = vk.method('newsfeed.get', {'count': count + offset, 'filters': 'post'})
            #pprint(m2['items'][((count + offset) % 100) - 1]['attachments'][0])
            return 'bad request'
#gl = Bot()
#tokken = '35db77277a6e00ea8035db2316ed190de24ca77c162c958eb72e83f70cc765b9a4d48dab35662aebfd65a'
#gl.public_posts(tokken, 0, 1, ['fd', 'fg', 'tr'], 'tnull')
#for i in range(1, 80):
#print(gl.get_filtered_news(tokken, i, 1, ['fd', 'fg', 'tr']))
