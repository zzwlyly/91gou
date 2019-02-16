from flask_restful import Resource, reqparse
from apps.cart.models import CartItem, CartOrder
from apps.ext import db
from apps.order.models import Orders, OrderItem
from apps.user.models import Address
from apps.utils.helper import product_code


class OrdersResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=int)

    #     todo 只结算每次点击的item
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

                        # 改变购物车item状态
                        cart.flag = 3
                        db.session.commit()

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
                    Orders.query.filter_by(oid=oid).update({'real_money': total_money})
                    db.session.commit()

                    # 返回订单数据
                    return oid
                    # order = Orders.query.filter(Orders.oid == oid).first()
                    # return to_response_success(data=order, fields=OrdersFields.result_fields)
                else:
                    return "False"
            else:
                return "False"
        except Exception as e:
            print(e)


class OrderStatusResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=str)
        self.parser.add_argument('oid', type=str)

    def get(self):
        uid = self.parser.parse_args().get('uid')
        oid = self.parser.parse_args().get('oid')

        try:
            # 支付成功后修改订单状态
            order = Orders.query.filter(Orders.oid == oid, Orders.uid == uid).first()
            if order:
                order.status = 0
                order.pay_status = 1
                db.session.commit()
            # 修改购物车&订单表状态
            cart_order = CartOrder.query.filter(CartOrder.oid == oid).all()
            for c_order in cart_order:
                cart_item = CartItem.query.filter(CartItem.cart_id == c_order.cart_id).first()
                cart_item.goods.sale_volume = cart_item.goods.sale_volume + cart_item.good_quantity
                cart_item.flag = 0
                # 修改商品销量
                db.session.commit()

            # todo 支付完成状态改完以后重定向跳转到一个页面

        except Exception as e:
            print(e)

    def post(self):
        uid = self.parser.parse_args().get('uid')
        oid = self.parser.parse_args().get('oid')

        try:
            # 支付成功后修改订单状态
            order = Orders.query.filter(Orders.oid == oid, Orders.uid == uid).first()
            if order:
                order.status = 0
                order.pay_status = 1
                db.session.commit()
            # 修改购物车&订单表状态
            cart_order = CartOrder.query.filter(CartOrder.oid == oid).all()
            for c_order in cart_order:
                cart_item = CartItem.query.filter(CartItem.cart_id == c_order.cart_id).first()
                cart_item.flag = 0
                db.session.commit()
        except Exception as e:
            print(e)
