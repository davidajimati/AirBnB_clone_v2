#!/usr/bin/python3
'''
starts a Flask web application:
    displays "Hello HBNB on port 5000
    "HBNB" on /hbnb
    /c/<text>: display “C ” followed by the value of
        the text variable (replace underscore _ symbols
        with a space )
'''

from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': ''}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    '''Displays "python is cool" -> by default
    or python (followed by text)
    '''
    if text is not '':
        res = text.replace("_", " ")
        return ("Python {}".format(res))
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''Displays "n is a number if it is" '''
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Displays "n is a number if it is" '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Displays "n is a number if it is" '''
    if n % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, type=type)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
