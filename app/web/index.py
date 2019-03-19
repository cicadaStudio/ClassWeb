from . import web
from flask import render_template, redirect, url_for


@web.route('/')
def index():
    return render_template('index.html')
