from flask import Flask
import json
from news_analyzer import get_popular_tags()


app = Flask(__name__)

@app.route('/')
def index():
    return 'WRONG PAGE!'


@app.route('/get_popular_tags', methods=['POST'])
def get_popular_tags():
    return json.dumps(get_popular_tags())

@app.route('/get_filtered_news', methods=['POST'])
def page_name():
    offset = flask.form['offset']
    token = flask.form['token']
    count = flask.form['count']
    tags = flask.form['tags']
    return json.dumps(get_filtered_news(token=token, offset=offset, count=count, tags=tags))

@app.route('/get_filtered_public_posts', methods=['POST'])
def page_name():
    offset = flask.form['offset']
    tok = flask.form['token']
    count = flask.form['count']
    public_id = flask.form['public_id']
    tags = flask.form['tags']
    return json.dumps(get_public_posts(token=token, offset=offset, count=count, tags=tags, public_id=public_id))

app.run('0.0.0.0', port=5000)
