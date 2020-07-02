from flask import render_template, url_for, flash, redirect, jsonify, request, Response, session
from quiz_app import app
from quiz_app import db

from quiz_app.models import Questions


@app.route("/index")
def index():
    "The index page"
    return "Hi Welcome"