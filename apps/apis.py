from flask_restful import Api

from apps.appraise.api import AppraiseResource
from apps.cart.api import CartResource
from apps.main.api import MainNavResource, MainCategoryResource
from apps.order.api import OrdersResource
from apps.product.api import GoodsResource
from apps.user.api import RegisterResource, LoginResource, AliPayResource, Test
from apps.product.api import GoodsResource, GoodsMainResource
from apps.user.api import RegisterResource, LoginResource
from apps.user.api import RegisterResource, LoginResource, AliPayResource

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


api.add_resource(AppraiseResource, '/appraise/')
api.add_resource(CartResource, '/cart/')

api.add_resource(MainNavResource, '/main/nav/')
api.add_resource(MainCategoryResource, '/main/cate/')

api.add_resource(OrdersResource, '/orders/')
api.add_resource(GoodsResource, '/goods/')
api.add_resource(GoodsMainResource, '/goods/main/')
api.add_resource(RegisterResource, '/register/')
api.add_resource(LoginResource, '/login/')
api.add_resource(AliPayResource, '/alipay/')
api.add_resource(Test, '/test/')
