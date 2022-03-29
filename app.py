from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LIS161'

@app.route('/', methods=["GET"])
def index():
    return render_template("home.html")