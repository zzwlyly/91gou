"""
评价表

id
uid 用户id
good_id 商品id
rating 评价等级 -1 差评 0 中评 1 好评
appraise_desc 评论内容
img1 评价照片
img2
img3
img4
img5
is_delete 0:删除 1:有效
create_time 创建时间
"""
import datetime

from apps.ext import db

# 用户评论表
from apps.user.models import User


class Appraise(db.Model):
    __tabelname__ = "appraise"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.ForeignKey(User.uid, ondelete="CASCADE"))
    good_id = db.Column(db.ForeignKey())  # TODO
    rating = db.Column(db.Integer)  # 等级
    appraise_desc = db.Column(db.Text)
    img1 = db.Column(db.String(255))
    img2 = db.Column(db.String(255))
    img3 = db.Column(db.String(255))
    img4 = db.Column(db.String(255))
    img5 = db.Column(db.String(255))
    is_delete = db.Column(db.Integer, default=1)  # 0:删除 1:有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
