from flask import Blueprint
from flask_restful import Api

from project.controllers.v1.accounts import Accounts
from project.controllers.v1.aggregation import ListOfVisitedOrLikedMedias, ListOfVisitedOrLikedAccounts
from project.controllers.v1.albums import Albums
from project.controllers.v1.filemanager import FileManager
from project.controllers.v1.follow import Follow
from project.controllers.v1.knock_knock import KnockKnock

# Create a new blueprint and add all controllers as resources.
from project.controllers.v1.like import Like
from project.controllers.v1.medias import Medias
from project.controllers.v1.singers import Singers
from project.controllers.v1.visit import Visit

api = Api()
api_bp = Blueprint('api', __name__, url_prefix='/v1')
api.init_app(api_bp)

# API Health Test:
api.add_resource(KnockKnock, '/knock_knock')

# Changelog CRUD:
api.add_resource(FileManager, '/file', '/file/<file_id>')
api.add_resource(Accounts, '/accounts', "/accounts/<account_id>")
api.add_resource(Singers, '/singers', "/singers/<singer_id>")
api.add_resource(Medias, '/medias', "/medias/<media_id>")
api.add_resource(Albums, '/albums', "/albums/<album_id>")
api.add_resource(Like, '/accounts/<account_id>/likes/<media_id>')
api.add_resource(Visit, '/accounts/<account_id>/visit/<media_id>')
api.add_resource(Follow, '/accounts/<account_id>/follow/<singer_id>')
api.add_resource(ListOfVisitedOrLikedMedias, '/aggregate/medias/liked/<account_id>')
api.add_resource(ListOfVisitedOrLikedAccounts, '/aggregate/accounts/liked/<media_id>')
