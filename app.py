from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LIS161'

@app.route('/', methods=["GET"])
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/home', methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/partnerships', methods=["GET"])
def partnerships():
    return render_template("partnerships.html")

@app.route('/minutes', methods=["GET"])
def minutes():
    return render_template("minutes.html")

@app.route('/announcements', methods=["GET"])
def announcements():
    return render_template("announcements.html")

@app.route('/registration', methods=["GET", "POST"])
def registration():
    return render_template("registration.html")

@app.route('/gallery', methods=["GET", "POST"])
def gallery():
    return render_template("gallery.html")

@app.route('/forum', methods=["GET", "POST"])
def forum():
    return render_template("forum.html")

@app.route('/calendar', methods=["GET"])
def calendar():
    return render_template("calendar.html")

@app.route('/memberdata', methods=["GET", "POST"])
def memberdata():
    return render_template("memberdata.html")

if __name__ == '__main__':
    app.run(debug=True)