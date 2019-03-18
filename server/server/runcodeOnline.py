#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

from pprint import pprint

def outputResult(code):
    url = 'https://m.runoob.com/api/compile.php'

    headers = {
            'Host': 'm.runoob.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://c.runoob.com/compile/6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Length': '88',
            'Origin': 'https://c.runoob.com',
            'DNT': '1',
            'Connection': 'keep-alive'
    }

    data = {
            'code':code,
            'stdin':'',
            'language':0,
            'fileext':'py'
    }

    r = requests.post(url, data=data, headers=headers)

    return (r.json())

if __name__ == "__main__":
    outputResult('print("heihei")')
