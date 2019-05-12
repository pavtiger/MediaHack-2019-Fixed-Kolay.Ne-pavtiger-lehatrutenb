from newsapi import NewsApiClient
from newsapi_secrets import newsapi_apikey
from time import time
import atexit
from selenium import webdriver
from datetime import datetime, timedelta
from pymorphy2 import MorphAnalyzer
from operator import itemgetter

class PopularTagsCollector:
    def __init__(self, apikey, update_interval_seconds=(60 * 60)):
        self.newsapi = NewsApiClient(apikey)
        self.update_interval = update_interval_seconds
        self.last_request = float('-inf')
        self.tags = set()

collector = PopularTagsCollector(newsapi_apikey)
opts = webdriver.chrome.options.Options()
opts.add_argument('--headless')
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')
assert opts.headless
browser = webdriver.Chrome(options=opts)
atexit.register(lambda: browser.quit())

def get_popular_tags():
    """ Returns a set of strings,
    each string is a tag """
    if(time() - collector.last_request < collector.update_interval):
        return collector.tags
    else:
        try:
            stop_words = []
            with open("stop words.txt", "r") as f:
                stop_words = f.read().split()
            top_headlines = collector.newsapi.get_top_headlines(language='ru')['articles']
            descriptions = ''.join([x for x in ' '.join(article['description'] for article in top_headlines) if (x.isalpha() or x in [' ', '-'])]).split()
            morphy = MorphAnalyzer()
            descriptions = [morphy.parse(x)[0].normal_form for x in descriptions]
            uniq = {}
            for word in descriptions:
                uniq[word] = uniq.get(word, 0) + 1
            sorted_uniq = sorted([(key, value) for key, value in uniq.items() if key not in stop_words], key=itemgetter(1))
            collector.tags = [i[0] for i in sorted_uniq[-10:]]
            collector.last_request = time()
        finally:
            return collector.tags

if __name__ == "__main__":
    collector = PopularTagsCollector(newsapi_apikey)
