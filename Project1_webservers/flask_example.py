# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 07:19:23 2023

@author: Joe
"""

from flask import Flask, request
from flask import __version__ as fv

app = Flask(__name__)

@app.route('/')
def hellow_world() -> str:
    
    '''
    
    Args:
        no arguements expected
    Returns:
        str: greetings message
    Note:
        uses 'request' global variable from flask module to read HTTP REST query params.
        if query params with key 'name' has no value, than uses 'World' as default
        
    '''
    
    name = request.args.get("name", "World")
    return "Hello, {}!".format(name)

@app.route('/version')
def version() -> str:
    '''
        Args:
            no arguments expected
        Returns:
            str: Flask Version
    '''
    return "Flask Version is {}".format(fv)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')