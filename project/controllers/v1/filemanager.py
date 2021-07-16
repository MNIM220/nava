import os
import uuid
from http import HTTPStatus

from flask import request, current_app, send_from_directory
from flask_restful import Resource

from config import ROOT_DIR


class FileManager(Resource):
    @staticmethod
    def post():
        file = request.files['data']
        filename = str(uuid.uuid4())
        if file:
            file.save(os.path.join(ROOT_DIR + "/filemanager", filename))

        return {'message': "Uploaded successfully", "file_id": filename}, HTTPStatus.OK

    @staticmethod
    def get(file_id):
        uploads = os.path.join(current_app.root_path, ROOT_DIR + "/filemanager")
        return send_from_directory(directory=uploads, filename=file_id)
