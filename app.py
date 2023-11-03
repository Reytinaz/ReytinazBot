from flask import Flask

app = Flask(__name__)

@app.route("/")
def keep_alive():
    return "Hello, World!"