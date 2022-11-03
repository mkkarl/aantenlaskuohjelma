from unittest import result
from db import db
from flask import session

class User:

    def __init__(self, id: int):
        self.__id = id

        sql = "SELECT username FROM users WHERE id=:id"
        result = db.session.execute(sql, {"id":id})
        user = result.fetchone()

        self.__username = user.username

        sql = "SELECT is_admin FROM users WHERE id=:id"
        result = db.session.execute(sql, {"id":id})
        is_admin = result.fetchone()

        self.__is_admin = user.is_admin
        
    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username