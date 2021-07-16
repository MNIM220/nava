from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class ListOfVisitedOrLikedMedias(Resource):
    @staticmethod
    def get(account_id):
        like_sql = "select media_id from likes where account_id = %s"
        visit_sql = "select media_id from visit where account_id = %s"
        val = tuple(account_id)

        mycursor = mysql_db.cursor()

        mycursor.execute(like_sql, val)
        like_result = mycursor.fetchall()

        mycursor.execute(visit_sql, val)
        visit_result = mycursor.fetchall()

        result = []
        for x in like_result:
            result.append(x[0])
        for x in visit_result:
            result.append(x[0])
        return {'medias': result}, HTTPStatus.OK


class ListOfVisitedOrLikedAccounts(Resource):
    @staticmethod
    def get(media_id):
        like_sql = "select account_id from likes where media_id = %s"
        visit_sql = "select account_id from visit where media_id = %s"
        val = tuple(media_id)

        mycursor = mysql_db.cursor()

        mycursor.execute(like_sql, val)
        like_result = mycursor.fetchall()

        mycursor.execute(visit_sql, val)
        visit_result = mycursor.fetchall()

        result = []
        for x in like_result:
            result.append(x[0])
        for x in visit_result:
            result.append(x[0])
        return {'accounts': result}, HTTPStatus.OK
