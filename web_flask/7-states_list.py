#!/usr/bin/python3
"""a prgram with flask"""

#from models import storage, State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def fun8():
    """a program with flask"""
    return storage.close()


@app.route('/states_list', strict_slashes=False)
def fun9():
    """a program with flask"""
    states = storage.all(State).values()
    return render_template('7-states_list.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
#    app.run()
