from flask_restful import Resource, reqparse

from apps.product.field import GoodsFields, GoodsMainFields
from apps.product.models import Goods, GoodsSKU, GoodsSPU, GoodsImages
from apps.utils.response_result import to_response_success


class GoodsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('good_id', type=str)
    '''
    商品详情api
    '''
    def get(self):
        good_id = self.parser.parse_args().get('good_id')
        goods = Goods.query.filter(Goods.good_id == good_id).first()

        return to_response_success(data=goods, fields=GoodsFields.result_fields)


class GoodsMainResource(Resource):
    '''
    首页商品api
    '''
    def get(self):
        goods = Goods.query.all()
        return to_response_success(data=goods, fields=GoodsMainFields.result_fields)