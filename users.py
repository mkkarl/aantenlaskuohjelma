from unittest import result
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password_hash, is_admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["user_is_admin"] = user.is_admin
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password_hash,is_admin) VALUES (:username, :password_hash, FALSE)"
        db.session.execute(sql, {"username":username, "password_hash":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)
    
def user_id():
    return session.get("user_id", 0)

def users_meeting_offices(meeting_id):
    sql = """SELECT users.id, users.username, O.meetingofficer, O.votecounter
        FROM
        users LEFT JOIN (SELECT * FROM officers WHERE meeting_id=:meeting_id) O ON users.id = O.user_id;"""
    result = db.session.execute(sql, {"meeting_id":meeting_id})
    users = result.fetchall()
    if not users:
        return False
    else:
        return users