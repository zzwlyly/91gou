import re
from alipay import AliPay
from flask import redirect
from flask_restful import Resource, reqparse
from apps import config
from apps.config import R
from apps.ext import db
from apps.user.field import UserMessageFields
from apps.utils.response_result import to_response_success
from apps.user.models import User, Vip, UserSafe


# 登录
from apps.user.models import User, Vip, UserSafe, Address

parser = reqparse.RequestParser()


class LoginResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str)
        self.parser.add_argument('password', type=str)
        self.parser.add_argument("id_session", type=int)
        # self.uid = None

    def post(self):
        data = self.parser.parse_args()
        # 前端携带session_id,核对redis,有就直接免密登录,没有就正常登录并保存session
        id_session = data.get("id_session")
        username = data.get("username")
        password = data.get("password")
        if id_session and R.sismember("user_sessions", id_session):
            # self.uid = uid
            # todo 返回数据
            return redirect('http://localhost:63343/91gou/main/main.html')
            # return to_response_success(data=data, fields=UserMessageFields.result_fields)
        else:
            # 判断用户登录类型(账号,手机,邮箱)
            user = self.check_name(username)
            uid = user.uid
            # self.uid = id
            if user:
                if user.verify_password(password):
                    R.sadd("user_sessions", user.uid)
                    R.expire("user_sessions", 24 * 60 * 60)
                    # user_data = User.query.filter(User.uid == id).first()
                    # return redirect(f'http://127.0.0.1:5000/api/v1/login/response/?uid={id}')
                    # return f'http://127.0.0.1:5000/api/v1/login/response/?uid={uid}'
                    return uid
                    # return to_response_success(data=user_data, fields=UserMessageFields.result_fields)
                else:
                    return 'login error~'
            else:
                return 'user not exist~'

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


class LoginResponseResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=int)
        super().__init__()

    def post(self):
        uid = self.parser.parse_args().get("uid")
        user_data = User.query.filter(User.uid == uid).first()
        return to_response_success(data=user_data, fields=UserMessageFields.result_fields)


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
                    return redirect("http://localhost:63343/91gou_html/main/login.html")
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


class AliPayResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('money', type=str)
        self.parser.add_argument('order_num', type=str)
        self.parser.add_argument('goods', type=str)

    def post(self):
        data = self.parser.parse_args()
        money = data.get("money")
        order_num = data.get("order_num")
        goods = data.get("goods")
        # 实例化Alipay对象
        alipay = AliPay(
            appid=config.APP_ID,
            app_notify_url=None,
            app_private_key_string=config.APP_PRIVATE_KEY_STR,
            alipay_public_key_string=config.APP_PUBLICK_KEY_STR,
            sign_type='RSA',
            debug=True,
        )

        # 生成支付的参数
        '''
        subject 支付的标题
        out_trade_no 生成的订单号
        total_amount 支付的总金额
        return_url  支付完成之后前端跳转的界面 get请求
        notify_url 支付完成后台回调接口  post请求
        '''
        order_str = alipay.api_alipay_trade_page_pay(
            subject=goods,
            out_trade_no=order_num,
            total_amount=money,
            return_url='https:www.baidu.com',
        )
        return redirect(config.PAY_URL_DEV + '?' + order_str)


class InformationUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nick_name', type=str)
        self.parser.add_argument('username', type=str)
        self.parser.add_argument('sex', type=int)
        self.parser.add_argument('birthday', type=str)
        self.parser.add_argument('telephone', type=str)
        self.parser.add_argument('email', type=str)
        self.uid = None

    def post(self):
        data = self.parser.parse_args()
        session_id = data.get('session_id')
        nick_name = data.get('nick_name')
        username = data.get('username')
        sex = data.get('sex')
        birthday = data.get('birthday')
        telephone = data.get('telephone')
        email = data.get('email')
        check_username = re.compile(r"^(?=.*?[a-z])\w{8,16}$")
        check_phone = re.compile(r"(^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7})$")
        check_email = re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
        try:
            if session_id and R.sismember("user_sessions", session_id):
                self.uid = session_id
                uid = self.uid
                users = User.query.filter(User.uid == uid,
                                          User.nick_name == nick_name,
                                          User.username == username,
                                          User.sex == sex,
                                          User.telephone == telephone,
                                          User.birthday == birthday,
                                          User.email == email
                                          ).first()
                if nick_name or username or sex or telephone or birthday or email:
                    if not users:
                        if check_username.match(username) and check_phone.match(telephone) and check_email.match(email):
                            user = User.query.filter_by(User.uid == uid).update({'nick_name': nick_name,
                                                                                 'username': username,
                                                                                 'sex': sex,
                                                                                 'birthday': birthday,
                                                                                 'telephone': telephone,
                                                                                 'email': email})
                            db.session.sommit()
                            data = "个人信息修改成功!请跳转登录页面!"
                            return to_response_success(data=data, fields=UserLoginFields.result_fields)
                        else:
                            return 'information error'
                    else:
                        return 'nothing update'
                else:
                    return 'not information'
            else:
                return 'user not find'
        except Exception as e:
            print(e)


class AddressUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('phone', type=str)
        self.parser.add_argument('detail', type=str)
        self.parser.add_argument('address', type=str)
        self.uid = None

    def post(self):
        data = self.parser.parse_args()
        session_id = data.get('session_id')
        name = data.get('name')
        phone = data.get('phone')
        detail = data.get('detail')
        address = data.get('address')
        check_phone = re.compile(r"(^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7})$")
        try:
            if session_id and R.sismember("user_sessions", session_id):
                self.uid = session_id
                uid = self.uid
                adr = Address.query.filter(Address.uid == uid,
                                           Address.name == name,
                                           Address.phone == phone,
                                           Address.detail == detail,
                                           Address.address == address)
                if not adr:
                    if check_phone.match(phone):
                        addre = Address(uid=uid,
                                        name=name,
                                        phone=phone,
                                        detail=detail,
                                        address=address)
                        db.session.add(addre)
                        db.session.commit()
                        data = "收货地址成功!请跳转登录页面!"
                        return to_response_success(data=data, fields=UserLoginFields.result_fields)
                    else:
                        return 'format error'
                else:
                    return "address is exist~"
            else:
                return 'user not find'
        except Exception as e:
            print(e)
