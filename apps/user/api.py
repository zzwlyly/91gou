import re

from flask_restful import Resource, reqparse

from apps.ext import db

__author__ = 'zhanjiahuan'
__date__ = '2019/1/21 10:58'

from flask import render_template, request, flash, Blueprint
from flask_login import login_user, login_required, logout_user

from apps.user.models import User

parser = reqparse.RequestParser()


class LoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        data = parser.parse_args()
        username = data.get("username")
        password = data.get("password")
        users = User.query.filter(
            User.username == username | User.email == username | User.telephone == username).first()
        if users:
            user = users
            if user._password == password:
                login_user(user, remember=True)
                return render_template("/")
            else:
                flash("账号或密码有误!请重新输入")
                return render_template('/')
        else:
            flash("用户不存在,请注册!")
            return render_template("/")


class RegisterResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        data = parser.parse_args()
        username = data.get("username")
        password = data.get("password")
        check_psw = data.get("check_psw")
        email = data.get("email")
        phone = data.get("phone")
        check_username = re.compile(r"^\w{8,16}$")
        check_password = re.compile(r"^\w{8,16}$")
        check_phone = re.compile(r"(^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7})$")
        check_email = re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
        users = User.query.filter(
            User.username == username | User.email == email | User.telephone == phone).first()
        if username and password and check_psw and email and phone:
            if not users:
                if check_username.search(username) and check_password.search(password) and \
                        check_phone.search(phone) and check_email.search(email):
                    user = User(username=username,email=email,telephone=phone)
                    user.password = password
                    db.session.add(user)
                    db.session.cimmit()
                    flash("注册成功!请登录!")
                    return render_template("/")
                else:
                    flash("请按正确的格式填写内容!")
                    return render_template("/")
            else:
                flash("用户已存在!")
                return render_template("/")
        else:
            flash("请填写全部内容!")
            return render_template("/")



