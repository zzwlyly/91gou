from flask_restful import Resource

from apps.product.models import Goods


class GoodsResource(Resource):
    def get(self):
        goods = Goods.query.all()
        return 'goods'
