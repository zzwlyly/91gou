from flask_restful import Api

from apps.appraise.api import AppraiseResource
from apps.cart.api import CartResource
from apps.main.api import MainResource
from apps.order.api import OrdersResource
from apps.product.api import GoodsResource
from apps.user.api import UserResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(AppraiseResource, '/appraise/')
api.add_resource(CartResource, '/cart/')
api.add_resource(MainResource, '/main/')
api.add_resource(OrdersResource, '/orders/')
api.add_resource(GoodsResource, '/goods/')
api.add_resource(UserResource, '/user/')
