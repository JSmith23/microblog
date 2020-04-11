from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Jimmy' }
    posts = [
        {
            'author': {'username': 'Jimmy'},
            'body': 'Beautiful day in Chicago!'
        },
        {
            'author': {'username': 'Goddess'},
            'body': 'Jimmy is my husband and who I look up to!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
