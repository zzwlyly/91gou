
# 购物车模型
import datetime

from apps.ext import db
from apps.user.models import User


class CartItem(db.Model):
    __tablename__ = "cart_item"
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    good_id = db.Column()#TODO
    good_quantity = db.Column(db.Integer) # 商品数量
    flag = db.Column(db.Integer, default=1)  # 0:未结算 1:已结算
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    user = db.relationship("User", backref="address", lazy="dynamic")

class CartOrder(db.Model):
    __tablename__ = "cart_order"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.ForeignKey(CartItem.cart_id,ondelete="CASCADE"))
    oid = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    car = db.relationship("CartItem",backref = "order",lazy = "dynamic")


