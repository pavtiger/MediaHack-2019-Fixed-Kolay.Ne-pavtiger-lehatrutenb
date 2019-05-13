import flask
import vericstrong
from news_analyzer import get_popular_tags
from f9 import get_filtered_news, get_filtered_public_posts

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'WRONG PAGE!'

@app.route('/get_popular_tags', methods=['GET', 'POST'])
def get_popular_tags_():
    return vericstrong.dumps(get_popular_tags())

@app.route('/get_filtered_news', methods=['GET', 'POST'])
def get_filtered_news_():
    rdata = {}
    if(flask.request.method == 'GET'):
        rdata = flask.request.args
    else:
        rdata = flask.request.form
    token = rdata['token']
    tags = rdata['tags']
    return vericstrong.dumps(get_filtered_news(token=token, tags=tags))

@app.route('/get_filtered_public_posts', methods=['GET', 'POST'])
def get_filtered_public_posts_():
    rdata = {}
    if(flask.request.method == 'GET'):
        rdata = flask.request.args
    else:
        rdata = flask.request.form
    token = rdata['token']
    public_id = rdata['public_id']
    tags = rdata['tags']
    return vericstrong.dumps(get_filtered_public_posts(token=token, tags=tags, public_id=public_id))

app.run('0.0.0.0', port=5000)
