from flask_restful import Resource

from apps.order.models import Orders


class OrdersResource(Resource):
    def get(self):
        orders = Orders.query.all()
        return 'orders'
