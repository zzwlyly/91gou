from flask_restful import Resource


class AppraiseResource(Resource):
    def get(self):
        return 'haha'
