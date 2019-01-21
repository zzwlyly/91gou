import datetime

from apps.ext import db

# 用户评论表
from apps.product.models import Goods
from apps.user.models import User


class Appraise(db.Model):
    __tabelname__ = "appraise"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    good_id = db.Column(db.Integer, db.ForeignKey(Goods.good_id, ondelete="CASCADE"))
    rating = db.Column(db.Integer)  # 等级
    appraise_desc = db.Column(db.Text)
    img1 = db.Column(db.String(255))
    img2 = db.Column(db.String(255))
    img3 = db.Column(db.String(255))
    img4 = db.Column(db.String(255))
    img5 = db.Column(db.String(255))
    is_delete = db.Column(db.Integer, default=1)  # 0:删除 1:有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
