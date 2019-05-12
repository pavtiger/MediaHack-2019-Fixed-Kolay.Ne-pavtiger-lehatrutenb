import vk_api
import urllib
from text_analyzer import check_text
from image_analyzer import check_picture

def get_filtered_news(token, tags, count=100):
    """
    :param token: string
    :param count: int(100)
    :param tags: ['', '', ''...]
    :return:
    filtered posts
    """

    vk = vk_api.VkApi(token=token)
    data = vk.method('newsfeed.get', {'count':count, 'filters':'post'})
    posts = data['items']

    for post in posts:
        text = post['text']

        if check_text(text, tags):
            post = None

        if 'attachments' in post.keys():
            for attachment in post['attachments']:
                if attachment['type'] == 'photo':
                    resource = urllib.urlopen(attachment['photo']['sizes'][-1]['url'])
                    output = open("file01.jpg", "wb")
                    output.write(resource.read())
                    output.close()

                    if check_picture('file01.jpg', tags):
                        post = None

    return [x for x in posts if x != None]

def get_filtered_public_posts(token, tags, pub_id, count=100):
    """
        :param token: string
        :param count: int(100)
        :param tags: ['', '', ''...]
        :return:
        filtered posts
        """
    vk = vk_api.VkApi(token=token)
    data = vk.method('newsfeed.get', {'count': count, 'filters': 'post', 'source_ids': pub_id})
    posts = data['items']

    for post in posts:
        text = post['text']

        if check_text(text, tags):
            post = None

        if 'attachments' in post.keys():
            for attachment in post['attachments']:
                if attachment['type'] == 'photo':
                    resource = urllib.urlopen(attachment['photo']['sizes'][-1]['url'])
                    output = open("file01.jpg", "wb")
                    output.write(resource.read())
                    output.close()

                    if check_picture('file01.jpg', tags):
                        post = None

    return [x for x in posts if x is not None]

if __name__ == "__main__":
    token = '1'
    #gl.public_posts(tokken, 0, 1, ['fd', 'fg', 'tr'], 'tnull')
    #print(get_filtered_news(token,  ['fd', 'fg', 'tr']))
    print(get_filtered_news_public_posts(token, ['fd', 'fg', 'tr'], 'tnull'))
