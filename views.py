from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


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
