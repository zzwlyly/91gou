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
    # goods = db.relationship("Goods", backref="shop", lazy="dynamic")


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
    # good_category = db.relationship("GoodCategory", backref="good_nav", lazy="dynamic")

    def __repr__(self):
        return self.name


# 首页导航分类
class GoodNavigation(db.Model):
    __tablename__ = "good_navigation"
    nid = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)  # 1:一级列表，2:二级，3:三级
    # sort = db.Column(db.Integer)  # 排序
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # good_category = db.relationship("GoodCategory", backref="good_nav", lazy="dynamic")

    def __repr__(self):
        return self.name


# 商品分类
class GoodCategory(db.Model):
    __tablename__ = "good_category"
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 外键
    # nid = db.Column(db.Integer)
    nid = db.Column(db.Integer, db.ForeignKey(GoodNavigation.nid, ondelete="CASCADE"))
    name = db.Column(db.String(64))
    cate_sort = db.Column(db.Integer)  # 排序
    is_show = db.Column(db.Integer)  # 0：隐藏 1：显示
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

    cate_property = db.relationship("GcProperty", backref="good_category", lazy="dynamic")
    goods = db.relationship("Goods", backref="good_category", lazy="dynamic")

    def __repr__(self):
        return self.name


# 商品分类属性表
class GcProperty(db.Model):
    __tablename__ = "cate_property"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 外键
    # cid = db.Column(db.Integer)
    cid = db.Column(db.Integer, db.ForeignKey(GoodCategory.cid, ondelete="CASCADE"))
    name = db.Column(db.String(255))
    values = db.Column(db.String(255))
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return self.name


class Banners(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(255))
    is_delete = db.Column(db.Integer)  # 0：删除 1：有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
