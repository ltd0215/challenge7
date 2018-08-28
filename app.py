#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, abort
import os.path
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/challenge7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)
    def __init__(self, title, created_time, category_time, content):
        self.title = title
        self.created_time = created_time
        self.category_time = category_time
        self.content = content
    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Category %r>' % self.name


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    title = File.query.all()
    return render_template('index.html', title=title)

@app.route('/files/<file_id>')
def file(file_id):
    content = File.query.get_or_404(file_id)

    return render_template('file.html', content=content)


