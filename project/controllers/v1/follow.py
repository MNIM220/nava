from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class Follow(Resource):
    @staticmethod
    def get(account_id, singer_id):
        sql = "INSERT INTO follow (account_id, singer_id) VALUES (%s, %s)"
        val = (account_id,
               singer_id)
        mycursor = mysql_db.cursor()
        mycursor.execute(sql, val)
        mysql_db.commit()
        return {'message': "Singer followed successfully"}, HTTPStatus.NO_CONTENT
