# added python comment
# added python comment
# added python comment
from flask import (Flask, request, url_for, send_from_directory, 
    jsonify, render_template, redirect, url_for, request, make_response)
from werkzeug.routing import BaseConverter
import json
from defaults import DEFAULTS
app = Flask(__name__, static_url_path="", static_folder='test-app/dist/test-app')

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

@app.route('/')
def index():
    return send_from_directory('test-app/dist/test-app/', 'index.html')

@app.route('/treehouse')
def treehouse_index():
    data = get_saved_data()
    return render_template('./index.html', saves = data)

@app.route('/treehouse_builder')
def treehouse_builder():
    print(DEFAULTS)
    return render_template('./builder.html', saves = get_saved_data(), options = DEFAULTS)

@app.route('/save', methods=['POST'])
def save():
    # import pdb
    # pdb.set_trace()
    response = make_response(redirect(url_for('treehouse_builder')))
    data = get_saved_data()
    print(dict(request.form.items()))
    form_items = dict(request.form.items())
    data.update(form_items)
    response.set_cookie('character', json.dumps(data))
    return response

@app.route("/<regex('\w\.(js|css)'):path>")
def angular_src(path):
    print("path: ", path)
    return send_from_directory('test-app/dist/test-app', path)

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return True
    else:
        return False

@app.route('/some-route')
def send_json():
    return jsonify({"test": 'Stefan'})


if __name__ == '__main__':
    app.run(debug=True, port=8080)