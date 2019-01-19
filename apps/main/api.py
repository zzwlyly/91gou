from flask_restful import Resource


class MainResource(Resource):
    def get(self):
        return 'haha'
