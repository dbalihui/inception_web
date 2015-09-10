# -*- coding:utf-8 -*-
#coding=utf-8
__author__ = 'xujing'

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.script import Manager

app = Flask(__name__)
# the toolbar is only enabled in debug mode:
app.debug = True
app.config.from_object('config')

toolbar = DebugToolbarExtension(app)
manager = Manager(app)

from app import views, forms
