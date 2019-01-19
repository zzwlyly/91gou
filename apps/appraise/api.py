from flask_restful import Resource

from apps.appraise.models import Appraise


class AppraiseResource(Resource):
    def get(self):
        appraises = Appraise.query.all()
        return 'haha'
