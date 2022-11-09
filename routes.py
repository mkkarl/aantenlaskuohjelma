from app import app
from flask import render_template, request, redirect
import users
from user import User
import meetings

@app.route("/")
def index():
    user_id = users.user_id()
    if user_id == 0:
        return redirect("/login")
    
    this_user = User(user_id)
    admin = this_user.get_is_admin

    return render_template("index.html", is_admin=admin)

@app.route("/login", methods=["GET", "POST"])
def login():
    # if users.user_id != 0:
    #     return redirect("/")
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    # if users.user_id() != 0:
    #     return redirect("/")
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/new_meeting", methods=["GET", "POST"])
def new_meeting():
    user_id = users.user_id()

    if user_id == 0:
        return redirect("/login")
    
    this_user = User(user_id)

    if this_user.get_is_admin:
        if request.method == "GET":
            return render_template("new_meeting.html")
        if request.method == "POST":
            meeting_name = request.form["meeting"]
            meeting_date = request.form["date"]
            meeting_time = request.form["time"]

            if meetings.new_meeting(meeting_name, meeting_date, meeting_time):
                return redirect("/")
            else:
                return render_template("error.html", message="Kokouksen luonti ei onnistunut")
    else:
        return redirect("/")

@app.route("/all_meetings")
def all_meetings():
    user_id = users.user_id()

    if user_id == 0:
        return redirect("/login")
    
    this_user = User(user_id)

    if this_user.get_is_admin:
        return render_template("all_meetings.html")
    else:
        return redirect("/")