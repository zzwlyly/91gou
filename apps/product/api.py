from flask_restful import Resource

from apps.product.field import GoodsFields, GoodsMainFields
from apps.product.models import Goods, GoodsSKU, GoodsSPU, GoodsImages
from apps.utils.response_result import to_response_success


class GoodsResource(Resource):
    def get(self):
        goods = Goods.query.all()

        return to_response_success(data=goods, fields=GoodsFields.result_fields)


class GoodsMainResource(Resource):
    def get(self):
        goods = Goods.query.all()

        return to_response_success(data=goods, fields=GoodsMainFields.result_fields)