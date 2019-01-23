# -*- coding:utf-8 -*-
from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__date__ = "2019/1/21 12:07"

from flask_restful import fields


class GoodsFields:
    good_fields = {
        'good_id': fields.String,
    }
    sku_fields = {
        'sku_id': fields.Integer,
        'good_id': fields.String,
    }

    spu_fields = {
        'spu_id': fields.Integer,
        'good_id': fields.String,
    }

    img_fields = {
        'img': fields.String,
        'good_id': fields.String,
    }
    # 数据结构的键名是模型字段名
    data_fields = {
        'goods': fields.List(fields.Nested(good_fields)),
        'sku': fields.List(fields.Nested(sku_fields)),
        'spu': fields.List(fields.Nested(spu_fields)),
        'img': fields.List(fields.Nested(img_fields)),
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(data_fields))
    }
