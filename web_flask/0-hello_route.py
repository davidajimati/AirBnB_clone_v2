#!/usr/bin/python3
"""
This module displays ` “Hello HBNB!”`
via 0.0.0.0 port 5000
"""
import flask as Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''returns Hello HBNB'''
    return ('Hello HBNB!')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
