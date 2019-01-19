from flask_restful import Resource

from apps.user.models import User


class UserResource(Resource):
    def get(self):
        user = User.query.all()
        return 'user'
