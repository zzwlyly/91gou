from flask_restful import Api

from apps.main.api import MainResource

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


api.add_resource(MainResource, '/main/')
