import datetime

from apps.ext import db

#     goods（商品表）
from apps.main.models import GoodCategory, GcProperty


class Goods(db.Model):
    __tablename__ = "goods"
    good_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey(GoodCategory.cid))
    shop_id = db.Column(db.Integer, db.ForeignKey(GcProperty.id))
    brand_id = db.Column(db.Integer)
    good_name = db.Column(db.String(255), nullable=False)
    stocks = db.Column(db.Integer)
    good_tips = db.Column(db.String(255), nullable=False)
    is_hot = db.Column(db.Integer)
    is_new = db.Column(db.Integer)
    is_recom = db.Column(db.Integer)
    is_sale = db.Column(db.Integer)
    good_desc = db.Column(db.String(255), nullable=False)
    good_status = db.Column(db.Integer)
    sale_volume = db.Column(db.Integer)
    sale_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# =============================================================================这是分界线

class GoodsSPU(db.Model):
    __tablename__ = "goods_spu"
    spu_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    good_id = db.Column(db.Integer, db.ForeignKey(GcProperty.id))
    spu_prop1 = db.Column(db.String(255))
    spu_prop2 = db.Column(db.String(255))
    spu_prop3 = db.Column(db.String(255))
    spu_prop4 = db.Column(db.String(255))
    spu_prop5 = db.Column(db.String(255))
    spu_prop6 = db.Column(db.String(255))
    spu_prop7 = db.Column(db.String(255))
    spu_prop8 = db.Column(db.String(255))
    spu_prop9 = db.Column(db.String(255))
    spu_prop10 = db.Column(db.String(255))
    spu_prop11 = db.Column(db.String(255))
    spu_prop12 = db.Column(db.String(255))
    spu_prop13 = db.Column(db.String(255))
    spu_prop14 = db.Column(db.String(255))
    spu_prop15 = db.Column(db.String(255))
    spu_prop16 = db.Column(db.String(255))
    spu_prop17 = db.Column(db.String(255))
    spu_prop18 = db.Column(db.String(255))
    spu_prop19 = db.Column(db.String(255))
    spu_prop20 = db.Column(db.String(255))
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    goods = db.relationship("Goods", backref="goods_spu", lazy="dynamic")


# =============================================================================这是分界线


class GoodsSKU(db.Model):
    __tablename__ = "goods_sku"
    sku_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    good_id = db.Column(db.Integer, db.ForeignKey(GcProperty.id))
    sku_name = db.Column(db.String(255))
    spu_prop1 = db.Column(db.String(255))
    spu_prop2 = db.Column(db.String(255))
    spu_prop3 = db.Column(db.String(255))
    spu_prop4 = db.Column(db.String(255))
    spu_prop5 = db.Column(db.String(255))
    original_price = db.Column(db.Numeric(10, 2))
    current_price = db.Column(db.Numeric(10, 2))
    show_img = db.Column(db.String(255))
    good_img = db.Column(db.String(255))
    good_stock = db.Column(db.Integer)
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    goods = db.relationship("Goods", backref="goods_sku", lazy="dynamic")
