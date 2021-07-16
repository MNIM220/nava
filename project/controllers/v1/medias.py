from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class Medias(Resource):
    @staticmethod
    def post():
        req = request.get_json()
        sql = "INSERT INTO medias (caption, media_name, produce_time, file_id, album_id) VALUES (%s, %s, %s, %s, %s)"
        val = (req.get("caption"),
               req.get("media_name"),
               req.get("produce_time"),
               req.get("file_id"),
               req.get("album_id"))
        mycursor = mysql_db.cursor()
        mycursor.execute(sql, val)
        mysql_db.commit()
        return {'message': "Media created successfully"}, HTTPStatus.NO_CONTENT

    @staticmethod
    def get(media_id):
        mycursor = mysql_db.cursor()

        val = tuple(media_id)
        mycursor.execute("select * from medias where id = %s", val)
        result = mycursor.fetchone()

        return {"result": {
            "id": result[0],
            "caption": result[1],
            "media_name": result[2],
            "produce_time": str(result[3]),
            "file_id": result[4],
            "album_id": result[5]
        }}, HTTPStatus.OK

    @staticmethod
    def put(media_id):
        mycursor = mysql_db.cursor()

        req = request.get_json()
        val = (req.get("caption"),
               req.get("media_name"),
               req.get("produce_time"),
               req.get("file_id"),
               req.get("album_id"),
               media_id)
        sql = "UPDATE medias set caption = %s, media_name = %s, produce_time = %s, file_id = %s, album_id = %s where id = %s"
        mycursor.execute(sql, val)

        mysql_db.commit()
        return {"message": "media successfully updated"}, HTTPStatus.NO_CONTENT
