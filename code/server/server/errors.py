# -*- coding: utf-8 -*-
from flask import jsonify

from server import app


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({ 'status':404 })


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({ 'status':500 })
