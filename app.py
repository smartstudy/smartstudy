#!/usr/bin/env python
import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
