# -*- coding:utf-8 -*-
from flask_restful import fields

from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__author__ = "zhou"
__date__ = "2019/1/24 13:56"


class OrdersFields:
    goods_fields = {
        'show_img': fields.String,
        'good_name': fields.String,
        'good_desc': fields.String,
        'good_price': fields.String,
        'sale_volume': fields.Integer,
    }

    items_fields = {
        'good_id': fields.String,
        'good_quantity': fields.String,
        'goods': fields.Nested(goods_fields)
    }

    order_fields = {
        'oid': fields.Integer,
        'create_time': fields.DateTime,
        'order_item': fields.List(fields.Nested(items_fields))
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(order_fields))
    }


# class CartItems:
#     order_fields = {
#         'oid': fields.Integer,
#         'create_time': fields.DateTime,
#         'order_item': fields.List(fields.Nested(items_fields))
#     }
#
#     result_fields = {
#         'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
#         'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
#         'data': fields.List(fields.Nested(order_fields))
#     }

class OrderSuccessFields:
    address_fields = {
        'aid': fields.Integer,
        'name': fields.String,
        'phone': fields.String,
        'address': fields.String,
        'detail': fields.String,
    }

    order_fields = {
        'oid': fields.Integer,
        'real_money': fields.Integer,
        'address': fields.Nested(address_fields)
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.Nested(order_fields)
    }
