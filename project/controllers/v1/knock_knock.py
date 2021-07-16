from http import HTTPStatus

from flask_restful import Resource

from project.extensions import mysql_db


class KnockKnock(Resource):
    @staticmethod
    def get():
        return "Who's there?", HTTPStatus.OK
