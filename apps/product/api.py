from flask_restful import Resource, reqparse

from apps.main.models import GoodCategory
from apps.product.field import GoodsFields, GoodsMainFields
from apps.product.models import Goods, GoodsSKU, GoodsSPU, GoodsImages
from apps.utils.response_result import to_response_success, to_response_error


class GoodsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('good_id', type=str)

    '''
    商品详情api
    '''

    def get(self):
        try:
            good_id = self.parser.parse_args().get('good_id')

            goods = Goods.query.filter(Goods.good_id == good_id).first()

            return to_response_success(data=goods, fields=GoodsFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()


class GoodsLimitResource(Resource):
    '''
    分类商品分页api
    '''

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nid', type=int)
        self.parser.add_argument('page', type=int, default=1)
        self.parser.add_argument('size', type=int, default=12)
        self.parser.add_argument("sort", type=int, default=1)

    def get(self):
        try:
            parser = self.parser.parse_args()
            nid = parser.get('nid')
            page = parser.get('page')
            size = parser.get('size')
            sort = parser.get("sort")

            cate = GoodCategory.query.filter(GoodCategory.nid == nid).first()
            if sort == 2:
                paginate = Goods.query.filter(Goods.cid == cate.cid)\
                    .order_by(-Goods.good_price)\
                    .paginate(page=page,per_page=size,error_out=False)
            elif sort == 3:
                paginate = Goods.query.filter(Goods.cid == cate.cid) \
                    .order_by(-Goods.sale_volume) \
                    .paginate(page=page, per_page=size, error_out=False)
            else:
                paginate = Goods.query.filter(Goods.cid == cate.cid).paginate(page=page, per_page=size, error_out=False)
            goods = paginate.items

            data = {
                'total': paginate.total,
                'pages': paginate.pages,
                'goods': goods,
            }

            return to_response_success(data=data, fields=GoodsMainFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()
