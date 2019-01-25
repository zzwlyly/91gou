from flask_restful import fields

from apps.order.field import OrdersFields
from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__author__ = 'zhanjiahuan'
__date__ = '2019/1/22 20:39'


class UserLoginFields:
    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.String
    }


class UserMessageFields:
    user_fields = {
        'username': fields.String,
        'user_photo': fields.String,
        'nick_name': fields.String,
        'name': fields.String,
        'sex': fields.Integer,  # 0男,1女
        'birthday': fields.DateTime,
        'telephone': fields.String,
        'email': fields.String,
        'flag': fields.Integer,  # 0 用户 1 商家

    }
    address_fields = {

        'name': fields.String,
        'phone': fields.String,
        'address': fields.String,
        'detail': fields.String,
    }
    user_safe_fields = {
        'safe_score': fields.Integer,
        'bind_phone': fields.Integer,
        'bind_email': fields.String,
        'id_card': fields.Integer,
        'real_name': fields.String,
        'front_img': fields.String,
        'reverse_img': fields.String,
        'question1': fields.String,
        'question2': fields.String,
    }
    vip_fields = {
        'vip_level': fields.Integer,
        'vip_score': fields.Integer,
    }

    data_fields = {
        'user': fields.List(fields.Nested(user_fields)),
        'address': fields.List(fields.Nested(address_fields)),
        'user_safe': fields.List(fields.Nested(user_safe_fields)),
        'vip': fields.List(fields.Nested(vip_fields)),
        'orders': fields.List(fields.Nested(OrdersFields.order_fields)),
        'cart_item': fields.List(fields.Nested(OrdersFields.order_fields)),
    }
    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.Nested(data_fields)
    }
