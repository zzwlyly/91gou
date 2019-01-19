from flask_restful import marshal, fields

from apps.utils.constant import *


def to_response_success(data, status=RESPONSE_SUCCESS_STATUS, msg=RESPONSE_SUCCESS_MSG, fields=None):
    result = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return marshal(result, fields)


error_result_fields = {
    'status': fields.Integer(default=RESPONSE_ERROR_STATUS),
    'msg': fields.String(default=RESPONSE_ERROR_MSG)
}


def to_response_error(status=RESPONSE_ERROR_STATUS, msg=RESPONSE_ERROR_MSG):
    result = {
        'status': status,
        'msg': msg,
    }
    return marshal(result, error_result_fields)
