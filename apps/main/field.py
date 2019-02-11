# -*- coding:utf-8 -*-
from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__date__ = "2019/1/21 12:07"

from flask_restful import fields


class MainNavFields:
    third_fields = {
        'nid': fields.Integer,
        'name': fields.String,
    }

    second_fields = {
        'nid': fields.Integer,
        'name': fields.String,
        'children': fields.List(fields.Nested(third_fields))
    }

    first_fields = {
        'nid': fields.Integer,
        'name': fields.String,
        'children': fields.List(fields.Nested(second_fields))
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(first_fields))
    }


class MainCategoryFields:
    property_fields = {
        'name': fields.String,
        'values': fields.String,
    }

    # goods_fields = {
    #     'cid': fields.Integer,
    #     'good_id': fields.String,
    #     'good_name': fields.String,
    #     'show_img': fields.String,
    #     'good_desc': fields.String,
    #     'good_price': fields.Integer,
    # }

    # 数据结构的键名是模型字段名
    data_fields = {
        'cid': fields.Integer,
        'nid': fields.Integer,
        'name': fields.String,
        # 绑定从表数据，根据关联关系查询...
        'cate_property': fields.List(fields.Nested(property_fields)),
        # 'goods': fields.List(fields.Nested(goods_fields)),
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(data_fields))
    }


class SearchFields:
    goods_fields = {
        'good_name': fields.String,
        'show_img': fields.String,
        'good_desc': fields.String,
        'good_price': fields.Integer,
    }
    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(goods_fields))
    }
