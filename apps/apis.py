from flask_admin import Admin
from flask_restful import Api

# from apps.ext import db, admin
from apps.appraise.api import AppraiseResource
from apps.cart.api import CartResource, CartDeleteResource
from apps.ext import admin, db

from apps.main.api import MainNavResource, MainCategoryResource, SearchResource, CategoryResource, \
    TestMainCategoryResource
from apps.main.models import GoodNav, GoodCategory, GcProperty
from apps.order.api import OrdersResource, OrderStatusResource
from apps.product.api import GoodsLimitResource
from apps.product.models import Goods
from apps.user.api import LogoutResource, InformationUser, AddressUser

from apps.product.api import GoodsResource
from apps.user.api import RegisterResource, LoginResource, AliPayResource, LoginResponseResource
from apps.user.models import User, Address

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


# ------------ 购物车 ------------ #
api.add_resource(CartResource, '/cart/')
api.add_resource(CartDeleteResource, '/cart/del/')

# ------------ 首页导航 ------------ #
api.add_resource(MainNavResource, '/main/nav/')

# ------------ 首页商品 ------------ #
api.add_resource(MainCategoryResource, '/main/cate/')
api.add_resource(TestMainCategoryResource, '/main/test/')

# ------------ 所有商品详情 ------------ #
api.add_resource(GoodsLimitResource, '/goods/limit/')

# ------------ 商品分类 ------------ #
api.add_resource(CategoryResource, '/cate/')

# ------------ 订单 ------------ #
api.add_resource(OrdersResource, '/orders/')
api.add_resource(OrderStatusResource, '/orders/status/')

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

# ------------ 修改个人信息 ------------ #
api.add_resource(InformationUser, '/information/')

# ------------ 添加收货地址 ------------ #
api.add_resource(AddressUser, '/address/')

"""
#######################后台管理################################
"""
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Goods, db.session))
# admin.add_view(ModelView(GoodNav, db.session))
# admin.add_view(ModelView(GoodCategory, db.session))
# admin.add_view(ModelView(GcProperty, db.session))

