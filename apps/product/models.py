import datetime

from apps.ext import db

#     goods（商品表）
from apps.main.models import GoodCategory, GcProperty


class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    good_id = db.Column(db.String(32), unique=True)

    cid = db.Column(db.Integer, db.ForeignKey(GoodCategory.cid))
    # shop_id = db.Column(db.Integer, db.ForeignKey(GcProperty.id))

    # 外键
    # cid = db.Column(db.Integer)
    shop_id = db.Column(db.Integer)
    brand_id = db.Column(db.Integer)
    ################
    good_name = db.Column(db.String(255), nullable=False)
    show_img = db.Column(db.String(255))
    good_desc = db.Column(db.String(255))
    good_price = db.Column(db.Numeric(11, 2))

    stocks = db.Column(db.Integer)
    good_tips = db.Column(db.String(255))
    is_hot = db.Column(db.Integer)
    is_new = db.Column(db.Integer)
    is_recom = db.Column(db.Integer)
    is_sale = db.Column(db.Integer)
    good_status = db.Column(db.Integer)
    sale_volume = db.Column(db.Integer)
    sale_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

    appraise = db.relationship("Appraise", backref="goods", lazy="dynamic")
    goods_spu = db.relationship("GoodsSPU", backref="goods", lazy="dynamic")
    goods_sku = db.relationship("GoodsSKU", backref="goods", lazy="dynamic")
    goods_img = db.relationship("GoodsImages", backref="goods", lazy="dynamic")


# =============================================================================这是分界线

class GoodsSPU(db.Model):
    __tablename__ = "goods_spu"
    spu_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # good_id = db.Column(db.String(32))
    good_id = db.Column(db.String(32), db.ForeignKey(Goods.good_id, ondelete="CASCADE"))

    spu_prop = db.Column(db.Text)
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# =============================================================================这是分界线


class GoodsSKU(db.Model):
    __tablename__ = "goods_sku"
    sku_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # good_id = db.Column(db.String(32))
    good_id = db.Column(db.String(32), db.ForeignKey(Goods.good_id, ondelete="CASCADE"))

    sku_name = db.Column(db.String(255))
    sku_prop = db.Column(db.String(255))
    original_price = db.Column(db.Numeric(10, 2))
    current_price = db.Column(db.Numeric(10, 2))
    good_stock = db.Column(db.Integer)
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


class GoodsImages(db.Model):
    __tablename__ = "goods_images"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # good_id = db.Column(db.String(32))
    good_id = db.Column(db.String(32), db.ForeignKey(Goods.good_id, ondelete="CASCADE"))

    img = db.Column(db.String(255))
    # 0:删除 1:有效
    is_delete = db.Column(db.Boolean, default=1)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
