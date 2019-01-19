from flask_restful import Api

from apps.main.api import MainResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(MainResource, '/main/')
