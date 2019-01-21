import datetime

from apps.ext import db
from apps.product.models import Goods
from apps.user.models import User, Address


# 订单表
class Orders(db.Model):
    __tabelname__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 订单号
    oid = db.Column(db.Integer, unique=True)
    # 用户id 外键 关联用户表
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    # 收货人id 外键  关联用户收货地址表
    aid = db.Column(db.Integer, db.ForeignKey(Address.aid, ondelete="CASCADE"))
    # 订单状态
    # -3:用户拒收 -2:未付款的订单 -1：用户取消 0:待发货 1:配送中 2:用户确认收货
    status = db.Column(db.Integer, default=-2)
    # 订单总金额
    total_money = db.Column(db.Numeric(11, 2))
    # 实际金额
    real_money = db.Column(db.Numeric(11, 2))
    # 支付方式
    # 0 在线支付/ 1 货到付款
    pay_type = db.Column(db.Integer)
    # 支付来源
    # 1 支付宝/2 微信/ 3  现金 pos机
    pay_from = db.Column(db.Integer)
    # 支付状态
    # 0:未支付 1:已支付
    pay_status = db.Column(db.Integer)
    # 订单成功所获取积分
    order_score = db.Column(db.Integer)
    # 订单备注
    remarks = db.Column(db.Text)
    # 是否退款
    # 0:否 1：是
    is_refund = db.Column(db.Integer)
    # 是否退货
    # 0:否 1：是  退货是指，商家退款，客户不用退货。客户已退货，商家退款
    is_return = db.Column(db.Integer)
    # 是否评价
    # 0:未点评 1:已点评
    is_appraise = db.Column(db.Integer)
    # 订单是否完结
    # 0：未完结 1:已完结
    is_closed = db.Column(db.Integer)
    # 订单创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # 订单支付时间
    pay_time = db.Column(db.DateTime)
    # 0:删除 1:有效
    is_delete = db.Column(db.Integer, default=1)
    # order_item = db.relationship("OrderItem", backref="Orders", lazy="dynamic")


# 订单内商品条目表
class OrderItem(db.Model):
    __tabelname__ = "order_item"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 外键  关联order订单表
    oid = db.Column(db.Integer, db.ForeignKey(Orders.oid, ondelete="CASCADE"))
    # 外键  关联User用户表
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    # 所购买的商品id
    good_id = db.Column(db.Integer)
    # 商品数量
    good_quantity = db.Column(db.Integer)


# 订单退款退货表
class OrderRefunds(db.Model):
    __tabelname__ = "order_refunds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 外键，订单id 关联order订单表
    oid = db.Column(db.Integer, db.ForeignKey(Orders.oid, ondelete="CASCADE"))
    # 退款人id  关联User用户表
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    # 退款商品id
    good_id = db.Column(db.Integer, db.ForeignKey(Goods.good_id, ondelete="CASCADE"))
    # 退款流水号
    refund_no = db.Column(db.String(32))
    # 退款备注
    refund_remark = db.Column(db.String(255))
    # 退款到账时间
    refund_time = db.Column(db.DateTime)
    # 退款原因
    refund_reason = db.Column(db.String(255))
    # 退款金额
    refund_money = db.Column(db.Numeric(11, 2))
    # 商家拒绝退款原因
    shop_reason = db.Column(db.String(255))
    # 退款状态
    # -1退款失败 / 0 审核中 / 1 退款成功
    refund_status = db.Column(db.Integer)
    # 退款发起时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
