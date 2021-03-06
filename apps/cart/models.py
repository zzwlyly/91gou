# 购物车模型
import datetime
from apps.ext import db
from apps.order.models import Orders
from apps.product.models import Goods
from apps.user.models import User


# 购物车表
class CartItem(db.Model):
    __tablename__ = "cart_item"
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    good_id = db.Column(db.String(32), db.ForeignKey(Goods.good_id))
    good_quantity = db.Column(db.Integer)  # 商品数量
    flag = db.Column(db.Integer, default=1)  # 0:已结算 1:添加到购物车 2:生成订单，未结算 3:支付中...
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    goods = db.relationship("Goods", backref="cart_item")


# 购物车订单详情表
class CartOrder(db.Model):
    __tablename__ = "cart_order"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey(CartItem.cart_id, ondelete="CASCADE"))
    oid = db.Column(db.Integer, db.ForeignKey(Orders.oid, ondelete="CASCADE"))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
