from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class Visit(Resource):
    @staticmethod
    def get(account_id, media_id):
        sql = "INSERT INTO visit (account_id, media_id) VALUES (%s, %s)"
        val = (account_id,
               media_id)
        mycursor = mysql_db.cursor()
        mycursor.execute(sql, val)
        mysql_db.commit()
        return {'message': "Media visited successfully"}, HTTPStatus.NO_CONTENT
