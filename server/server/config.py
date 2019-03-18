# -*- coding: utf-8 -*-
import os
import sys

from server import app


SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
