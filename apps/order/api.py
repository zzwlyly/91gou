from flask_restful import Resource, reqparse
from werkzeug.utils import redirect

from apps.cart.models import CartItem, CartOrder
from apps.ext import db
from apps.order.field import OrderSuccessFields
from apps.order.models import Orders, OrderItem
from apps.product.models import Goods
from apps.user.models import Address
from apps.utils.helper import product_code
from apps.utils.response_result import to_response_success, to_response_error


class OrdersResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=int)

    # TODO 2.1 购物车界面点击结算后生成订单
    def post(self):
        uid = self.parser.parse_args().get('uid')
        # cart_id = self.parser.parse_args().get('cart_id')
        try:
            # TODO 2.2 【获取购物车数据】生成订单：购物车点结算的时候改变了flag状态，通过用户id去查找所有符合flag状态的商品
            carts = CartItem.query.filter(CartItem.uid == uid,
                                          CartItem.flag == 2,
                                          ).all()
            if uid:
                if carts:
                    # 生成订单单号
                    oid = product_code()
                    # TODO 订单生成的时候先默认第一个用户，后面确认订单的时候根据用户选择修改
                    user_ads = Address.query.filter(Address.uid == uid and Address.is_delete == 1).first()
                    aid = user_ads.aid
                    # TODO 2.3 生成订单，保存数据到order表
                    new_order = Orders(oid=oid, uid=uid, aid=aid)
                    db.session.add(new_order)
                    db.session.commit()

                    # TODO 2.3 关联订单和购物车数据
                    for cart in carts:
                        good_id = cart.good_id
                        cart_id = cart.cart_id
                        good_quantity = cart.good_quantity

                        # TODO 2.4 改变购物车item状态，这样下次就不会重复加入到订单里了
                        cart.flag = 3
                        db.session.commit()

                        # 保存数据到cart_order表
                        cart_order = CartOrder(oid=oid, cart_id=cart_id)
                        db.session.add(cart_order)
                        db.session.commit()

                        # 保存数据到order_item表（订单item数据表的数据和购物车order表是多对多关系，所以可以放一个循环里
                        order_item = OrderItem(oid=oid, uid=uid, good_id=good_id, good_quantity=good_quantity)
                        db.session.add(order_item)
                        db.session.commit()

                    # TODO 2.5 保存订单商品总价到order表
                    total_money = 0
                    order_item_goods = OrderItem.query.filter(OrderItem.oid == oid).all()
                    for order_item_good in order_item_goods:
                        total_money += int(order_item_good.goods.good_price) * int(order_item_good.good_quantity)
                    Orders.query.filter_by(oid=oid).update({'real_money': total_money})
                    db.session.commit()

                    # TODO 2.6 返回订单号，支付界面需要用
                    return oid
                    # order = Orders.query.filter(Orders.oid == oid).first()
                    # return to_response_success(data=order, fields=OrdersFields.result_fields)
                else:
                    return "False"
            else:
                return "False"
        except Exception as e:
            print(e)


# TODO 4. 支付成功后前端发送post请求，修改订单数据
class OrderStatusResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('uid', type=str)
        self.parser.add_argument('oid', type=int)

    def post(self):
        # uid = self.parser.parse_args().get('uid')
        oid = self.parser.parse_args().get('oid')

        try:
            # 支付成功后修改订单状态
            # order = Orders.query.filter(Orders.oid == oid, Orders.uid == uid).first()
            order = Orders.query.filter(Orders.oid == oid).first()
            if order:
                order.status = 0
                order.pay_status = 1
                db.session.commit()
            # 修改购物车&订单表状态
            cart_order = CartOrder.query.filter(CartOrder.oid == oid).all()
            for c_order in cart_order:
                cart_item = CartItem.query.filter(CartItem.cart_id == c_order.cart_id).first()

                if cart_item.goods.sale_volume is None:
                    cart_item.goods.sale_volume = 0
                cart_item.goods.sale_volume = int(cart_item.goods.sale_volume) + int(cart_item.good_quantity)

                cart_item.flag = 0
                # 修改商品销量
                db.session.commit()

        except Exception as e:
            print(e)


class AddOrderItemGoodsQuantity(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=str)
        self.parser.add_argument('oid', type=str)
        self.parser.add_argument('good_id', type=str)
        self.parser.add_argument('quantity', type=str)

    def post(self):
        uid = self.parser.parse_args().get('uid')
        oid = self.parser.parse_args().get('oid')
        good_id = self.parser.parse_args().get('good_id')
        quantity = self.parser.parse_args().get('quantity')

        order_item = OrderItem.query.filter(OrderItem.uid == uid, OrderItem.oid == oid,
                                            OrderItem.good_id == good_id).first()
        cart_item = CartItem.query.filter(CartItem.uid == uid, OrderItem.good_id == good_id,
                                          CartItem.flag == 2).first()
        good = Goods.query.filter(Goods.good_id == good_id).first()
        order = Orders.query.filter(Orders.uid == uid, Orders.oid == oid).first()

        if order_item and cart_item:
            original_price = order_item.good_quantity * good.good_price
            price = good.good_price * int(quantity)
            if original_price > price:
                order.real_money = order.real_money - (original_price - price)
                # db.session.commit()
            elif original_price < price:
                order.real_money = order.real_money + (price - original_price)
                # db.session.commit()
            order_item.good_quantity = int(quantity)
            # db.session.commit()
            cart_item.good_quantity = int(quantity)
            db.session.commit()


class OrderSuccessResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('oid', type=str)

    def post(self):
        oid = self.parser.parse_args().get('oid')

        try:
            order = Orders.query.filter(Orders.oid == oid, Orders.status == 0).first()
            return to_response_success(data=order, fields=OrderSuccessFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()
