from unittest import result
from db import db

def new_meeting(meeting_name, meeting_date, meeting_time):
    try:
        sql = "INSERT INTO meetings (meeting_name,meeting_date,meeting_time) VALUES (:meeting_name, :meeting_date, :meeting_time)"
        db.session.execute(sql, {"meeting_name":meeting_name,"meeting_date":meeting_date,"meeting_time":meeting_time})
        db.session.commit()
    except:
        return False
    return True

def all_meetings():
    sql = "SELECT id, meeting_name, meeting_date, meeting_time FROM meetings"
    result = db.session.execute(sql)
    meetings = result.fetchall()
    return meetings