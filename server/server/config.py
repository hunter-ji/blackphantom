# -*- coding: utf-8 -*-
import os
import sys

from server import app


SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))

# mariadb
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABSE = 'server'
USERNAME = 'username'
PASSWORD = 'passwd'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABSE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

# sqlite3
# dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path), 'data.db')
