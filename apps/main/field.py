# -*- coding:utf-8 -*-
from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__date__ = "2019/1/21 12:07"

from flask_restful import fields


class MainNavFields:

    third_fields = {
        'nid': fields.Integer,
        'name': fields.String,
        'sort': fields.Integer
    }

    second_fields = {
        'nid': fields.Integer,
        'name': fields.String,
        'sort': fields.Integer,
        'third': fields.List(fields.Nested(third_fields))
    }

    data_fields = {
        'nid': fields.Integer,
        'name': fields.String,
        'sort': fields.Integer,
        # 'cate': fields.List(fields.Nested(second_fields))
    }

    # data_fields = {
    #     'nid': fields.Integer,
    #     'name': fields.String,
    #     'sort': fields.Integer,
    # }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(data_fields))
    }
