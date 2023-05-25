#!/usr/bin/env python3
'''
starts a Flask web application:
    displays "Hello HBNB on port 5000
    and HBNB on /hbnb
'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Displays "Hello HBNB" '''
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays "HBNB" '''
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
