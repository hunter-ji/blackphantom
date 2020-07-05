#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import random
import sys

sys.path.append("./test/")


def filter(code):
    """Filter dangerous shell commands.

    :param code : Code source.
    :type code : str

    :return : Return 1 when all is ok.
    :type return : int
    """
    words = ['rm -rf', 'rm /', ':(){:|:&};:', '/dev', '^foo^bar']
    for key in words:
        if key in code and 'os' in code:
            return 1


def localoutputResult(code):
    """Run the code locally and output the result.

    :param code : Code source.
    :type code : str

    :return : Result type and result.
    :type return : json
    """
    if filter(code):
        return { 'output': '', "errors": 'error...' }
    haserror = 0
    front = str(random.randint(0, 1000)) + str(random.randint(0, 1000)) + \
            str(random.randint(0, 1000))
    behind = str(time.time()).split('.')[1]

    filename = front + behind + '.py'

    with open(filename, 'w') as f:
        f.write(code)
    try:
        L = []
        # Use python to test the framework pytest and get all the output.
        result = os.popen('pytest %s -s' % (filename)).readlines()
        for i in result:
            if 'ERRORS' in i:
                haserror = 1
            L.append(str(i))
        R = []
        if haserror == 1:
            for i in range(7, len(L) - 2):
                R.append(L[i])
        else:
            for i in range(3, len(L) - 3):
                R.append(L[i])
        L = ('<br>').join(R)
        L = L.replace(' ', '&nbsp;')
        result = { 'output': L, 'errors': '' }
    except Exception as e:
        result = { 'output': '', 'errors': e }
    finally:
        os.system('rm %s' % (filename))
        print(result)
    return result
