from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class Albums(Resource):
    @staticmethod
    def post():
        req = request.get_json()
        sql = "INSERT INTO albums (title, produce_time, genre) VALUES (%s, %s, %s)"
        val = (req.get("title"),
               req.get("produce_time"),
               req.get("genre"))
        mycursor = mysql_db.cursor()
        mycursor.execute(sql, val)
        mysql_db.commit()
        return {'message': "Album created successfully"}, HTTPStatus.NO_CONTENT

    @staticmethod
    def get(album_id):
        mycursor = mysql_db.cursor()

        val = tuple(album_id)
        mycursor.execute("select * from albums where id = %s", val)
        result = mycursor.fetchone()

        return {"result": {
            "id": result[0],
            "title": result[1],
            "produce_time": str(result[2]),
            "genre": result[3]
        }}, HTTPStatus.OK

    @staticmethod
    def put(album_id):
        mycursor = mysql_db.cursor()

        req = request.get_json()
        val = (req.get("title"),
               req.get("produce_time"),
               req.get("genre"),
               album_id)
        sql = "UPDATE albums set title = %s, produce_time = %s, genre = %s where id = %s"
        mycursor.execute(sql, val)

        mysql_db.commit()
        return {"message": "album successfully updated"}, HTTPStatus.NO_CONTENT
