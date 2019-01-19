import datetime

from apps.ext import db
from apps.user.models import User


# 商家店铺
class Shop(db.Model):
    __tablename__ = "shop"
    shop_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    shop_name = db.Column(db.String(64))
    is_self = db.Column(db.Integer)  # 0：自营 1：非自营
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# 品牌表
class Brand(db.Model):
    __tablename__ = "brand"
    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(64))
    brand_img = db.Column(db.String(255))
    brand_desc = db.Column(db.Text)
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# 首页导航分类
class GoodNav(db.Model):
    __tablename__ = "good_nav"
    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(64))
    level = db.Column(db.Integer)  # 1:一级列表，2:二级，3:三级
    sort = db.Column(db.Integer)  # 排序
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# 商品分类
class GoodCategory(db.Model):
    __tablename__ = "good_category"
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nid = db.Column(db.Integer, db.ForeignKey(GoodNav.nid, ondelete="CASCADE"))
    name = db.Column(db.String(64))
    brand = db.Column(db.Integer)  # 分类等级
    cate_sort = db.Column(db.Integer)  # 排序
    is_show = db.Column(db.Integer)  # 0：隐藏 1：显示
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    good_nav = db.relationship("GoodNav", backref="category", lazy="dynamic")


# 商品分类属性表
class GcProperty(db.Model):
    __tablename__ = "cate_property"
    gid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cid = db.Column(db.Integer, db.ForeignKey(GoodCategory.cid, ondelete="CASCADE"))
    name = db.Column(db.String(255))
    values = db.Column(db.String(255))
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    good_nav = db.relationship("GoodNav", backref="cate_prop", lazy="dynamic")
