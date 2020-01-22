#!/usr/bin/python3
"""a prgram with flask"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def fun():
    """a program with flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def fun2():
    """a program with flask"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def fun3(text):
    """a program with flask"""
    return "C %s" % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def fun4(text="is cool"):
    """a program with flask"""
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def fun5(n):
    """a program with flask"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def fun6(n):
    """a program with flask"""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
