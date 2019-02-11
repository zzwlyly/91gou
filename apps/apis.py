from flask_restful import Api
from apps.appraise.api import AppraiseResource
from apps.cart.api import CartResource
from apps.main.api import CategoryResource
from apps.main.api import MainNavResource, MainCategoryResource, SearchResource
from apps.order.api import OrdersResource
from apps.product.api import GoodsResource, GoodsLimitResource
from apps.user.api import LoginResponseResource, LogoutResource
from apps.user.api import RegisterResource, LoginResource, AliPayResource

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


# ------------ 购物车 ------------ #
api.add_resource(CartResource, '/cart/')

# ------------ 首页导航 ------------ #
api.add_resource(MainNavResource, '/main/nav/')

# ------------ 首页商品 ------------ #
api.add_resource(MainCategoryResource, '/main/cate/')

# ------------ 所有商品详情 ------------ #
api.add_resource(GoodsLimitResource, '/goods/limit/')

# ------------ 商品分类 ------------ #
api.add_resource(CategoryResource, '/cate/')

# ------------ 订单 ------------ #
api.add_resource(OrdersResource, '/orders/')

# ------------ 商品详情 ------------ #
api.add_resource(GoodsResource, '/goods/')

# ------------ 登录/注册 ------------ #
api.add_resource(RegisterResource, '/register/')
api.add_resource(LoginResource, '/login/')
api.add_resource(LoginResponseResource, '/login/response/')
api.add_resource(LogoutResource, '/logout/')

# ------------ 评论 ------------ #
api.add_resource(AppraiseResource, '/appraise/')

# ------------ 支付 ------------ #
api.add_resource(AliPayResource, '/alipay/')

# ------------ 搜索 ------------ #
api.add_resource(SearchResource, '/search/')

# api.add_resource(InformationUser, '/information/')
# api.add_resource(AddressUser, '/address/')
