import json
import signal
import subprocess
import sys
import redis

from flask import Flask, jsonify, request, current_app
from flask_cors import CORS
from flask_pymongo import PyMongo
from config import DevConfig, DefaultConfig
import mysql.connector
from project.extensions import changelogs, current_config, flask_app, mongo_client, mysql_db
from project.helpers.exceptions import NotFoundError, ForbiddenError, InternalServiceError, ValidationError

default_app_name = 'Changelog'
logger = None


def create_app(config=None, app_name=default_app_name):
    """
    Creates a new Flask app and sets up everything.

    :param config: Config class for the app
    :type config: class

    :param app_name: App name
    :type app_name: str

    :returns: A new Flask app object
    :rtype: Flask
    """
    current_config.set(config or DefaultConfig)
    app = Flask(app_name)
    flask_app.set(app)
    configure_cors(app)
    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
    configure_custom_errors(app)
    configure_before_request(app)

    return app


def configure_cors(app):
    """
    Enables CORS for the given app.

    :param app: Flask app object
    :type: app: Flask
    """
    CORS(app, resources={
        r'/*': {
            'origins': '*',
            'expose_headers': [
                'X-ACCESS-TOKEN',
                'X-EXPIRES-IN',
                'X-REFRESH-TOKEN',
                'X-TOKEN-TYPE'
            ]
        }
    }, supports_credentials=True)


def configure_app(app, config):
    """
    Sets Flask app config.
    Uses DevConfig if no config is given.

    :param app: Flask app object
    :type: app: Flask

    :param config: Config class
    :type config: class
    """
    if config is not None:
        app.config.from_object(config)
    else:
        app.config.from_object(DevConfig)


def configure_blueprints(app):
    """
    Creates and registers a blueprint for each API version.

    :param app: Flask app object
    :type app: Flask
    """
    api_versions = app.config['API_VERSIONS']
    for api_version in api_versions:
        blueprints = __import__('project.controllers.{}'.format(api_version), fromlist=[api_version])
        app.register_blueprint(blueprints.api_bp)


def configure_extensions(app):
    """
    Configures all extensions used by this Flask app.

    :param app: Flask app
    :type app: Flask
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nava"
    )
    mysql_db.set(mydb)


def configure_custom_errors(app):
    """
    Defines response patterns for when custom exceptions are raised.
    Custom exceptions are registered to Flask's error handler.

    :param app: Flask app object
    :type app: Flask
    """

    @app.errorhandler(InternalServiceError)
    def internal_error(error):
        _error = error.service_error if error.status_code != 500 else 'متاسفانه سرویس داخلی با مشکل مواجه شده‌است'
        if isinstance(_error, bytes):
            _error = _error.decode('utf-8')
        try:
            _error = json.loads(_error)
        except:
            _error = dict(message=_error)
        if error.error:
            err_msg = _error.get('message', '')
            if err_msg:
                _error['message'] = error.error + '\r\n' + _error['message']
            else:
                _error['message'] = error.error
        return jsonify(_error), error.status_code

    @app.errorhandler(NotFoundError)
    def validation_error(error):
        _error = dict(message='اطلاعات مورد نظر یافت نشد')
        if error.field and error.error:
            _error['errors'] = {
                error.field: [error.error]
            }
        elif error.error:
            _error['message'] = error.error
        return jsonify(_error), 404

    @app.errorhandler(ForbiddenError)
    def validation_error(error):
        _error = dict(message='شما به این قسمت دسترسی ندارید')
        if error.field and error.error:
            _error['errors'] = {
                error.field: [error.error]
            }
        elif error.error:
            _error['message'] = error.error
        return jsonify(_error), 403

    @app.errorhandler(ValidationError)
    def validation_error(error):
        _error = dict(message='اطلاعات ارسالی معتبر نمی‌باشد')
        if error.field and error.error:
            _error['errors'] = {
                error.field: [error.error]
            }
        elif error.error:
            _error['message'] = error.error
        return jsonify(_error), 400


def configure_before_request(app):
    """
    Defines a method to execute for each request context before requests are handled by controllers.

    :param app: Flask app object
    :type app: Flask
    """

    @app.before_request
    def print_requests():
        # Print request body.
        if request.data:
            print('Request body:')
            print(request.data.decode(encoding='utf-8'))
