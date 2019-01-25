from flask_restful import Resource, reqparse
from apps.ext import db
from apps.cart.models import CartItem


class CartResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=str)
        self.parser.add_argument('good_id', type=str)
        self.parser.add_argument('quantity', type=int, default=1)

    def get(self):
        items = CartItem.query.all()
        return 'cart'

    # TODO 购物车中添加商品
    def post(self):
        good_id = self.parser.parse_args().get('good_id')
        uid = self.parser.parse_args().get('uid')
        quantity = self.parser.parse_args().get('quantity')
        shopcar = CartItem.query.filter(CartItem.uid == uid, CartItem.good_id == good_id, CartItem.flag == 1).first()
        try:
            if shopcar is None:
                # 保存到购物车表中
                shopcar = CartItem(
                    uid=uid,
                    good_id=good_id,
                    good_quantity=quantity
                )
                db.session.add(shopcar)
                db.session.commit()

            #  TODO 当购物车中已存在当前商品时
            else:
                try:
                    shopcar.good_quantity = int(quantity) + int(shopcar.good_quantity)
                    db.session.commit()

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

    # # TODO 删除购物车中的商品
    # def delete(self,):
    #     parser = reqparse.RequestParser()
    #     gooddel_id= parser.parse_args().get('good_id')
    #     shopcardetail =CartItem.query.filter(CartItem.good_id==gooddel_id).all()
    #     try:
    #         db.session.delete(shopcardetail)
    #         db.session.commit()
    #
    #     except Exception as e:
    #         print(e)

    '''
    动态获取购物车中的商品数量
    并修改表中的商品数量
    '''
