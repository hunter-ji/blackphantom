# -*- coding: utf-8 -*-
from flask import Flask

app = Flask('server')
app.config.from_pyfile('config.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from server import views, errors
