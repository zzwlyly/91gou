import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from apps.ext import db


# 用户表
class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    _password = db.Column(db.String(255), nullable=False)
    user_photo = db.Column(db.String(128))
    nick_name = db.Column(db.String(64))
    name = db.Column(db.String(64))
    sex = db.Column(db.Integer)  # 0男,1女
    birthday = db.Column(db.DateTime)
    telephone = db.Column(db.String(64))
    email = db.Column(db.String(64))
    flag = db.Column(db.Integer)  # 0 用户 1 商家
    is_delete = db.Column(db.Integer, default=1)  # 0:删除 1:有效
    is_active = db.Column(db.Integer,default=0)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

    appraise = db.relationship("Appraise", backref="user", lazy="dynamic")

    address = db.relationship("Address", backref="user", lazy="dynamic")
    orders = db.relationship("Orders", backref="user", lazy="dynamic")
    order_refunds = db.relationship("OrderRefunds", backref="user", lazy="dynamic")
    cart_item = db.relationship("CartItem", backref="user", lazy="dynamic")

    def get_id(self):
        return self.uid

    @property
    def password(self):
        return self._password

    # 加密
    @password.setter
    def password(self, password):
        if password:
            self._password = generate_password_hash(password)
        else:
            raise Exception('password is not null')

    # 验证密码
    def verify_password(self, password):
        return check_password_hash(self._password, password)


# 用户地址表
class Address(db.Model):
    __tablename__ = "address"
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    name = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    address = db.Column(db.String(255))
    detail = db.Column(db.Text)
    is_delete = db.Column(db.Integer, default=1)  # 0:删除 1:有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# 用户安全设置表
class UserSafe(db.Model):
    __tablename__ = "user_safe"
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    safe_score = db.Column(db.Integer)
    password = db.Column(db.String(64), nullable=False)
    pay_pwd = db.Column(db.String(32))
    bind_phone = db.Column(db.Integer)
    bind_email = db.Column(db.String(64))
    id_card = db.Column(db.Integer)
    real_name = db.Column(db.String(16))
    front_img = db.Column(db.String(255))
    reverse_img = db.Column(db.String(255))
    question1 = db.Column(db.String(255))
    question2 = db.Column(db.String(255))
    answer1 = db.Column(db.String(255))
    answer2 = db.Column(db.String(255))
    is_delete = db.Column(db.Integer, default=1)  # 0:删除 1:有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())


# vip表
class Vip(db.Model):
    __tablename__ = "vip"
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"))
    vip_level = db.Column(db.Integer)
    vip_score = db.Column(db.Integer)
    is_delete = db.Column(db.Integer, default=1)  # 0:删除 1:有效
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

# if __name__ == '__main__':
#     pwd = 'a123456'
#     user = User(username='zhanjiahuan', password=pwd)
