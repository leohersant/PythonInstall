# Entry point (server file)
# This file contains only routes

# imports
from flask import Flask, render_template, json


# initialize app
app = Flask(__name__)

# routes
@app.route('/')
def index():
    return render_template('home.html')

# needed to debug and launch app: pytho app.py
if __name__ == '__main__':
    app.run(debug=True)