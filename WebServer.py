import flask
import json
from news_analyzer import get_popular_tags
from f9 import get_filtered_news, get_filtered_public_posts

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'WRONG PAGE!'


@app.route('/get_popular_tags', methods=['POST'])
def get_popular_tags_():
    return json.dumps(get_popular_tags())

@app.route('/get_filtered_news', methods=['POST'])
def get_filtered_news_():
    offset = flask.request.form['offset']
    token = flask.request.form['token']
    count = flask.request.form['count']
    tags = flask.request.form['tags']
    return json.dumps(get_filtered_news(token=token, offset=offset, count=count, tags=tags))

@app.route('/get_filtered_public_posts', methods=['POST'])
def get_filtered_public_posts_():
    offset = flask.request.form['offset']
    token = flask.request.form['token']
    count = flask.request.form['count']
    public_id = flask.request.form['public_id']
    tags = flask.request.form['tags']
    return json.dumps(get_filtered_public_posts(token=token, offset=offset, count=count, tags=tags, public_id=public_id))

app.run('0.0.0.0', port=5000)
