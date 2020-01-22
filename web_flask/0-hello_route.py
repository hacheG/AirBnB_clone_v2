#!/usr/bin/python3
"""a prgram with flask"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def fun():
    """a program with flask"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= "5000")