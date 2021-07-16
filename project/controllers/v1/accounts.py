from http import HTTPStatus

from flask import request
from flask_restful import Resource

from project.extensions import mysql_db


class Accounts(Resource):
    @staticmethod
    def post():
        req = request.get_json()
        sql = "INSERT INTO accounts (first_name, last_name, birth_date, biography, picture_id, email) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (req.get("first_name"),
               req.get("last_name"),
               req.get("birth_date"),
               req.get("biography"),
               req.get("picture_id"),
               req.get("email"))
        mycursor = mysql_db.cursor()
        mycursor.execute(sql, val)
        mysql_db.commit()
        return {'message': "Account created successfully"}, HTTPStatus.NO_CONTENT

    @staticmethod
    def get(account_id):
        mycursor = mysql_db.cursor()

        val = tuple(account_id)
        mycursor.execute("select * from accounts where id = %s", val)
        result = mycursor.fetchone()

        return {"result": {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "birth_date": str(result[3]),
            "biography": result[4],
            "picture_id": result[5],
            "email": result[6],
        }}, HTTPStatus.OK

    @staticmethod
    def put(account_id):
        mycursor = mysql_db.cursor()

        req = request.get_json()
        val = (req.get("first_name"),
               req.get("last_name"),
               req.get("birth_date"),
               req.get("biography"),
               req.get("picture_id"),
               req.get("email"),
               account_id)
        sql = "UPDATE accounts set first_name = %s, last_name = %s, birth_date = %s, biography = %s, picture_id = %s, email = %s where id = %s"
        mycursor.execute(sql, val)

        mysql_db.commit()
        return {"message": "account successfully updated"}, HTTPStatus.NO_CONTENT
