import os
import sys

from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, url_for
from flask_sslify import SSLify

load_dotenv(find_dotenv(usecwd=True))

app = Flask(__name__)
sslify = SSLify(app)


# MAIN HANDLERS
@app.route("/")
def render_home_page():
    """
    Renders the home page from jinja2 template
    """
    try:
        return render_template("index.html")
    except BaseException:
        return render_template("index.html")

if __name__ == "__main__":
    app.debug = False
    # app.run(host='0.0.0.0', port=9999)
