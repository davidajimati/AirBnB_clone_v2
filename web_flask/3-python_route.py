#!/usr/bin/python3
'''
starts a Flask web application:
    displays "Hello HBNB on port 5000
    "HBNB" on /hbnb
    /c/<text>: display “C ” followed by the value of
        the text variable (replace underscore _ symbols
        with a space )
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''Displays "C and text" '''
    res = text.replace("_", " ")
    return ("C {}".format(res))


@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    '''Displays "python is cool" -> by default
    or python (followed by text)
    '''
    if not text:
        return "Python is cool"
    res = text.replace("_", " ")
    return ("Python {}".format(res))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
