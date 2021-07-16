from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class Singers(Resource):
    @staticmethod
    def post():
        req = request.get_json()
        sql = "INSERT INTO singers (first_name, last_name, birth_date, biography, picture_id) VALUES (%s, %s, %s, %s, %s)"
        val = (req.get("first_name"),
               req.get("last_name"),
               req.get("birth_date"),
               req.get("biography"),
               req.get("picture_id"))
        mycursor = mysql_db.cursor()
        mycursor.execute(sql, val)
        mysql_db.commit()
        return {'message': "Singer created successfully"}, HTTPStatus.NO_CONTENT

    @staticmethod
    def get(singer_id):
        mycursor = mysql_db.cursor()

        val = tuple(singer_id)
        mycursor.execute("select * from singers where id = %s", val)
        result = mycursor.fetchone()

        return {"result": {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "birth_date": str(result[3]),
            "biography": result[4],
            "picture_id": result[5]
        }}, HTTPStatus.OK

    @staticmethod
    def put(singer_id):
        mycursor = mysql_db.cursor()

        req = request.get_json()
        val = (req.get("first_name"),
               req.get("last_name"),
               req.get("birth_date"),
               req.get("biography"),
               req.get("picture_id"),
               singer_id)
        sql = "UPDATE singers set first_name = %s, last_name = %s, birth_date = %s, biography = %s, picture_id = %s where id = %s"
        mycursor.execute(sql, val)

        mysql_db.commit()
        return {"message": "singer successfully updated"}, HTTPStatus.NO_CONTENT
