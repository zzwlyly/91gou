import re

from flask_restful import Resource, reqparse

from apps.ext import db

__author__ = 'zhanjiahuan'
__date__ = '2019/1/21 10:58'

from flask import render_template, request, flash, Blueprint, redirect
from flask_login import login_user, login_required, logout_user

from apps.user.models import User

parser = reqparse.RequestParser()


class LoginResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, location='form')
        self.parser.add_argument('password', type=str, location='form')

    def check_name(self, username):
        check_username = re.compile(r"^\w{8,16}")
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
        # global user
        data = self.parser.parse_args()
        username = data.get("username")
        password = data.get("password")
        # 判断用户登录类型(账号,手机,邮箱)
        user = self.check_name(username)
        if user:
            if user.verify_password(password):
                login_user(user, remember=True)
                return 'login success!'
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
        check_username = re.compile(r"^\w{8,16}")
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
                    # flash("注册成功!请登录!")
                    return "success"
                else:
                    # flash("请按正确的格式填写内容!")
                    return 'format error~'
            else:
                # flash("用户已存在!")
                return "user is exist~"
        else:
            # flash("请填写全部内容!")
            return 'incomplete data~'
