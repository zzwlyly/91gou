import re
from threading import Thread
from flask import session, request
from flask_restful import Resource, reqparse
from apps import config
from apps.config import R
from apps.ext import db
from apps.user.field import UserLoginFields, UserMessageFields
from apps.utils.response_result import to_response_success

__author__ = 'zhanjiahuan'
__date__ = '2019/1/21 10:58'

from flask_login import login_user, login_required, logout_user

from apps.user.models import User, Address, Vip, UserSafe

parser = reqparse.RequestParser()


class LoginResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str)
        self.parser.add_argument('password', type=str)
        self.parser.add_argument("id_session", type=int)

    # 实现手机,账号,邮箱都能登录
    def check_name(self, username):
        check_username = re.compile(r"^(?=.*?[a-z])\w{8,16}$")
        check_phone = re.compile(r"(^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7})$")
        check_email = re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
        if check_username.match(username):
            user = User.query.filter(User.username == username).first()
            return user
        elif check_phone.match(username):
            user = User.query.filter(User.telephone == username).first()
            return user
        elif check_email.match(username):
            user = User.query.filter(User.email == username).first()
            return user

    def post(self):
        data = self.parser.parse_args()
        # 前端携带session_id,核对redis,有就直接免密登录,没有就正常登录并保存session
        uid = data.get("id_session")
        username = data.get("username")
        password = data.get("password")
        if uid and R.sismember("user_session", uid):
            user = User.query.filter(User.uid == uid)
            login_user(user, remember=True)
            return "直接跳转首页"
        else:
            # 判断用户登录类型(账号,手机,邮箱)
            user = self.check_name(username)
            if user:
                if user.verify_password(password):
                    login_user(user, remember=True)
                    R.sadd("user_sessions", user.uid)
                    R.expire("user_sessions", 24 * 60 * 60)
                    data = user.uid
                    return to_response_success(data=data, fields=UserLoginFields.result_fields)
                else:
                    return 'login error~'
            else:
                return 'user not exist~'


class RegisterResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, location='form')
        self.parser.add_argument('password', type=str, location='form')
        self.parser.add_argument('password_repeat', type=str, location='form')
        self.parser.add_argument('email', type=str, location='form')
        self.parser.add_argument('phone', type=str, location='form')
        super().__init__()

    def post(self):
        data = self.parser.parse_args()
        user_name = data.get("username")
        password = data.get("password")
        check_psw = data.get("password_repeat")
        email = data.get("email")
        phone = data.get("phone")
        check_username = re.compile(r"^(?=.*?[a-z])\w{8,16}$")
        check_password = re.compile(r"^[a-zA-Z]\w{5,17}$")
        check_phone = re.compile(r"(^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7})$")
        check_email = re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
        users = User.query.filter(
            User.username == user_name, User.email == email, User.telephone == phone).first()
        if user_name and password and check_psw and email and phone:
            if not users:
                if check_username.match(user_name) and check_password.match(password) and \
                        check_phone.match(phone) and check_email.match(email):
                    user = User(username=user_name, email=email, telephone=phone)
                    user.password = password
                    db.session.add(user)
                    db.session.commit()
                    data = "注册成功!请跳转登录页面!"
                    return to_response_success(data=data, fields=UserLoginFields.result_fields)
                else:
                    # flash("请按正确的格式填写内容!")
                    return 'format error~'
            else:
                # flash("用户已存在!")
                return "user is exist~"
        else:
            # flash("请填写全部内容!")
            return 'incomplete data~'


# 用户账号邮箱验证激活
# import yagmail
#
#
# def send_mail(mail):
#     # 链接邮箱服务器
#     yag = yagmail.SMTP(user="zhanjiahuan123@163.com", password="python1805", host='smtp.163.com')
#
#     # 邮箱正文
#     contents = ['This is the body, and here is just text http://somedomain/image.png',
#                 'You can find an audio file attached.', '/local/path/song.mp3']
#
#     # 发送邮件
#     yag.send(mail, '文档', contents)

# 用户信息数据 注释部分待配合前端测试
class UserMessageResource(Resource):
    # def __init__(self):
    #     self.parser = reqparse.RequestParser()
    #     self.parser.add_argument('uid', type=int)

    def get(self):
        # data = self.parser.parse_args()
        # uid = data.get("uid")
        user = User.query.filter(User.uid == 1).all()
        address = Address.query.filter(Address.uid == 1).all()
        user_safe = UserSafe.query.filter(UserSafe.uid == 1).all()
        vip = Vip.query.filter(Vip.uid == 1)
        data = {
            "user": user,
            "address": address,
            "user_safe": user_safe,
            "vip": vip,
        }
        return to_response_success(data=data, fields=UserMessageFields.result_fields)
