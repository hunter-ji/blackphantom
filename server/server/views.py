# -*- coding: utf-8 -*-
import json

from flask import make_response, jsonify, json, request

from server import app

from server.runcode import localoutputResult


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = json.loads(request.get_data()).get('code')
        data = jsonify(localoutputResult(code))
        res = make_response(data)
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return res
    return jsonify( { 'mes' : 1 } )
