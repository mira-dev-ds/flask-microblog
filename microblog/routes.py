from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mirunalini'}

    posts = [
        {
            'author': {'username': 'Shoba'},
            'body': 'Beautiful day in Chennai!'
        },
        {
            'author': {'username': 'Anand'},
            'body': 'Flask is awesome!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)