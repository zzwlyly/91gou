from flask_restful import Resource

from apps.cart.models import CartItem


class CartResource(Resource):
    def get(self):
        items = CartItem.query.all()
        return 'cart'
