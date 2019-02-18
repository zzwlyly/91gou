from flask_restful import Resource, reqparse

from apps.ext import db
from apps.cart.models import CartItem


class CartResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=str)
        self.parser.add_argument('good_id', type=str)
        self.parser.add_argument('quantity', type=str)
        # self.parser.add_argument('quantity', type=int, default=1)

    # TODO ====== 在商品详情页点击加入购物车前先查询是否有该商品，如果有则查询出数量增加 ======
    def get(self):

        good_id = self.parser.parse_args().get('good_id')
        uid = self.parser.parse_args().get('uid')
        shop_car = CartItem.query.filter(CartItem.uid == uid, CartItem.good_id == good_id,
                                         CartItem.flag == 1).first()
        if shop_car:
            return shop_car.good_quantity
        else:
            return 0

    # TODO【登录后购物流程】 ====== 1. 往购物车里添加商品 ======
    def post(self):
        good_id = self.parser.parse_args().get('good_id')
        uid = self.parser.parse_args().get('uid')
        quantity = self.parser.parse_args().get('quantity')

        good_id = good_id.split(',')
        if quantity is not None:
            quantity = quantity.split(',')

        for i in range(len(good_id)):
            shopcar = CartItem.query.filter(CartItem.uid == uid, CartItem.good_id == good_id[i],
                                            CartItem.flag == 1).first()
            if quantity is None:
                # TODO 2. 点击了结算，还未支付，先修改购物车条目状态（方便订单数据的获取生成和防止重复加入订单）
                shopcar.flag = 2
                db.session.commit()
            else:
                try:
                    # TODO 1.1 购物车里没有要添加的商品，则创建数据条目
                    if shopcar is None:
                        # 保存到购物车表中
                        shopcar = CartItem(
                            uid=uid,
                            good_id=good_id[i],
                            good_quantity=quantity[i]
                        )
                        db.session.add(shopcar)
                        db.session.commit()

                    # TODO 1.2 当购物车中已存在当前商品时则只增加数量
                    else:
                        try:
                            shopcar.good_quantity = int(quantity[i])
                            db.session.commit()

                        except Exception as e:
                            print(e)

                except Exception as e:
                    print(e)

    '''
    动态获取购物车中的商品数量
    并修改表中的商品数量
    '''


# TODO 1.3 删除购物车中的商品
class CartDeleteResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=str)
        self.parser.add_argument('good_id', type=str)

    def post(self):
        good_id = self.parser.parse_args().get('good_id')
        uid = self.parser.parse_args().get('uid')

        shopcar = CartItem.query.filter(CartItem.uid == uid, CartItem.good_id == good_id,
                                        CartItem.flag == 1).first()
        try:
            if shopcar:
                db.session.delete(shopcar)
                db.session.commit()
        except Exception as e:
            print(e)
