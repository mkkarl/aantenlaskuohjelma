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

        
        
    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def get_is_admin(self):

        sql = "SELECT is_admin FROM users WHERE id=:id"
        result = db.session.execute(sql, {"id":self.__id})

        is_admin = result.fetchone().is_admin
        
        return is_admin