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
    }
    order_fields = {
        'oid': fields.Integer,
        'good_quantity': fields.String,
        'goods': fields.Nested(goods_fields)
    }
    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(order_fields))
    }
