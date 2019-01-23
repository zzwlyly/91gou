from flask_restful import fields

from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG

__author__ = 'zhanjiahuan'
__date__ = '2019/1/22 20:39'


class UserFields:
    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.String
    }
