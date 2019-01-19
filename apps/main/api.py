from flask_restful import Resource

from apps.main.models import GoodNav


class MainResource(Resource):
    def get(self):
        good_nav = GoodNav.query.all()
        return 'main'
