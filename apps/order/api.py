from flask_restful import Resource, reqparse
from apps.cart.models import CartItem, CartOrder
from apps.ext import db
from apps.order.field import OrdersFields
from apps.order.models import Orders, OrderItem
from apps.user.models import Address
from apps.utils.helper import product_code
from apps.utils.response_result import to_response_success, to_response_error


class OrdersResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=int)
        self.parser.add_argument('cart_id', type=int)

    # def get(self):
    # 返回订单数据
    # order = Orders.query.filter(Orders.oid == 124292935).first()
    # order = Orders.query.filter(Orders.uid == 1).all()
    # order_items = OrderItem.query.filter(OrderItem.uid == uid).all()

    # return to_response_success(data=order, fields=OrdersFields.result_fields)
    # uid = self.parser.parse_args().get('uid')
    # try:
    #     order_item = OrderItem.query.filter(OrderItem.uid == uid).all()
    #     return to_response_success(data=order_item, fields=OrdersFields.result_fields)
    # except Exception as e:
    #     print(e)
    #     return to_response_error()

    def post(self):
        uid = self.parser.parse_args().get('uid')
        # cart_id = self.parser.parse_args().get('cart_id')
        try:
            carts = CartItem.query.filter(CartItem.uid == uid,
                                          CartItem.flag == 2,
                                          ).all()
            if uid:
                if carts:
                    # 生成订单单号
                    oid = product_code()
                    user_ads = Address.query.filter(Address.uid == uid and Address.is_delete == 1).first()
                    aid = user_ads.aid
                    # todo 根据所有商品id查到订单表需要的商品内容并添加
                    # 保存数据到order表
                    new_order = Orders(oid=oid, uid=uid, aid=aid)
                    db.session.add(new_order)
                    db.session.commit()

                    for cart in carts:
                        good_id = cart.good_id
                        cart_id = cart.cart_id
                        good_quantity = cart.good_quantity

                        # 保存数据到cart_order表
                        cart_order = CartOrder(oid=oid, cart_id=cart_id)
                        db.session.add(cart_order)
                        db.session.commit()

                        # 保存数据到order_item表
                        order_item = OrderItem(oid=oid, uid=uid, good_id=good_id, good_quantity=good_quantity)
                        db.session.add(order_item)
                        db.session.commit()

                    # 保存订单商品总价到order表
                    total_money = 0
                    order_item_goods = OrderItem.query.filter(OrderItem.oid == oid).all()
                    for order_item_good in order_item_goods:
                        total_money += int(order_item_good.goods.good_price) * int(order_item_good.good_quantity)
                    new_orders = Orders.query.filter_by(oid=oid).update({'total_money': total_money})
                    db.session.commit()

                    # 返回订单数据
                    # order = Orders.query.filter(Orders.oid == oid).first()
                    # return to_response_success(data=order, fields=OrdersFields.result_fields)
                else:
                    return "False"
            else:
                return "False"
        except Exception as e:
            print(e)
