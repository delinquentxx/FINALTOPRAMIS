from flask import Flask, render_template, request
from data import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LIS161'

@app.route('/', methods=["GET"])
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/processing', methods=['post'])
def processing():
    account_SID = request.form['regstudentid']
    account_email = request.form['regemail']
    account_password = request.form['regpassword']

    account_data = {'SID': account_SID,
                    'email': account_email,
                    'password': account_password}
    insert_account(account_data)
    return render_template("login.html")

@app.route('/dashboard', methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

@app.route('/partnerships', methods=["GET"])
def partnerships():
    return render_template("partnerships.html")

@app.route('/minutes', methods=["GET"])
def minutes():
    return render_template("minutes.html")

@app.route('/announcements', methods=["GET"])
def announcements():
    return render_template("announcements.html")


@app.route('/create', methods=["GET"])
def create():
    return render_template("create.html")

@app.route('/process_announcement', methods=['post'])
def process_announcement():
    announcement_date = request.form['date']
    announcement_committee = request.form['committee']
    announcement_message = request.form['announcement_text']

    announcement_data = {'date': announcement_date,
                    'committee': announcement_committee,
                    'message': announcement_message}
    insert_announcement(announcement_data)
    return render_template("dashboard.html")

@app.route('/delete_announcement', methods=['GET'])
def delete_announcement():
    return render_template("delete_announcement.html")

@app.route('/process_delete_announcement', methods=['post'])
def process_delete_announcement():
    announcement_id = request.form['AID']
    process_deleting_announcement(announcement_id)
    return render_template("dashboard.html")

@app.route('/registration', methods=["GET", "POST"])
def registration():
    return render_template("registration.html")

@app.route('/gallery', methods=["GET", "POST"])
def gallery():
    return render_template("gallery.html")

@app.route('/upload_new_picture', methods=["GET"])
def upload_new_picture():
    return render_template("upload_new_picture.html")

@app.route('/process_new_picture', methods=['post'])
def process_new_picture():
    picture_date = request.form['date']
    picture_image = request.form['image']
    picture_details = request.form['image_details']

    image_data = {'date': picture_date,
                    'image': picture_image,
                    'details': picture_details}
    insert_picture(image_data)
    return render_template("gallery.html")





@app.route('/forum', methods=["GET", "POST"])
def forum():
    return render_template("forum.html")

@app.route('/calendar', methods=["GET"])
def calendar():
    return render_template("calendar.html")

@app.route('/profile', methods=["GET"])
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    app.run(debug=True)