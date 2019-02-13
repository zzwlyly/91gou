# -*- coding:utf-8 -*-
from apps.user.field import UserMessageFields
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

    user_fields = {
        'username': fields.String,
        'user_photo': fields.String,
    }

    appraise_fields = {
        'rating': fields.Integer,
        'appraise_desc': fields.String,
        'img2': fields.String,
        'img3': fields.String,
        'img4': fields.String,
        'img5': fields.String,
        'img6': fields.String,
        'create_time':fields.DateTime,
        'user': fields.Nested(user_fields),
    }

    # 数据结构的键名是模型字段名
    data_fields = {
        'cid': fields.Integer,
        'good_id': fields.String,
        'good_name': fields.String,
        'show_img': fields.String,
        'good_desc': fields.String,
        'good_price': fields.Integer,
        'sale_volume': fields.Integer,
        'goods_sku': fields.List(fields.Nested(sku_fields)),
        'goods_spu': fields.List(fields.Nested(spu_fields)),
        'goods_img': fields.List(fields.Nested(img_fields)),
        'appraise': fields.List(fields.Nested(appraise_fields)),
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
        'sale_volume': fields.Integer,
    }

    data = {
        'total': fields.Integer,
        'pages': fields.Integer,
        'goods': fields.List(fields.Nested(data_fields)),
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.Nested(data)
    }
