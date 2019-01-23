from flask_restful import Resource

from apps.product.field import GoodsFields
from apps.product.models import Goods, GoodsSKU, GoodsSPU, GoodsImages
from apps.utils.response_result import to_response_success


class GoodsResource(Resource):
    def get(self):
        goods = Goods.query.all()
        skus = GoodsSKU.query.all()
        spus = GoodsSPU.query.all()
        imgs = GoodsImages.query.all()

        data_fields = {
            'goods': goods,
            'sku': skus,
            'spu': spus,
            'img': imgs,
        }

        return to_response_success(data=data_fields, fields=GoodsFields.result_fields)

        # good_fields = []
        # sku_fields=[]
        # for good in goods:
        #     print(good.good_id)
        #     for sku in skus:
        #         if good.good_id == sku.good_id:
        #             sku_fields.append(sku)
        #         good_fields.append({'good_id': good.good_id, 'sku': sku_fields})
        # print(good_fields)
        # return 'goods'
