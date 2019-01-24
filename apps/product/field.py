# -*- coding:utf-8 -*-
from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__date__ = "2019/1/21 12:07"

from flask_restful import fields


class GoodsFields:
    sku_fields = {
        'sku_name': fields.String,
        'current_price': fields.Integer,
        'good_stock': fields.Integer,
    }

    spu_fields = {
        'spu_prop': fields.String,
    }

    img_fields = {
        'img': fields.String,
    }
    # 数据结构的键名是模型字段名
    data_fields = {
        'cid': fields.Integer,
        'good_id': fields.String,
        'good_name': fields.String,
        'show_img': fields.String,
        'good_desc': fields.String,
        'good_price': fields.Integer,
        'goods_sku': fields.List(fields.Nested(sku_fields)),
        'goods_spu': fields.List(fields.Nested(spu_fields)),
        'goods_img': fields.List(fields.Nested(img_fields)),
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(data_fields))
    }


class GoodsMainFields:

    # 数据结构的键名是模型字段名
    data_fields = {
        'cid': fields.Integer,
        'good_id': fields.String,
        'good_name': fields.String,
        'show_img': fields.String,
        'good_desc': fields.String,
        'good_price': fields.Integer,
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(data_fields))
    }
