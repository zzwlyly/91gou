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

    def get(self):
        uid = self.parser.parse_args().get('uid')
        try:
            order_item = OrderItem.query.filter(OrderItem.uid == uid).all()
            return to_response_success(data=order_item, fields=OrdersFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()

    def post(self):
        uid = self.parser.parse_args().get('uid')
        cart_id = self.parser.parse_args().get('cart_id')
        try:
            cart = CartItem.query.filter(CartItem.uid == uid,
                                         CartItem.cart_id == cart_id
                                         ).first()
            if uid and cart_id:
                if cart:
                    # 生成订单单号
                    oid = product_code()
                    good_id = cart.good_id
                    good_quantity = cart.good_quantity
                    user_ads = Address.query.filter(Address.uid == uid and Address.is_delete == 1).first()
                    aid = user_ads.aid
                    order = Orders(oid=oid, uid=uid, aid=aid)
                    db.session.add(order)
                    db.session.commit()
                    cart_item = CartOrder(oid=oid, cart_id=cart_id)
                    db.session.add(cart_item)
                    db.session.commit()
                    order_item = OrderItem(oid=oid, uid=uid, good_id=good_id, good_quantity=good_quantity)
                    db.session.add(order_item)
                    db.session.commit()
                    return "success"
                else:
                    return "False"
            else:
                return "False"
        except Exception as e:
            print(e)
