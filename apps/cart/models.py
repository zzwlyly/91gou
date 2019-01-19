"""
购物车模型

cart_id
	主键
uid
	外键，用户id
status
	用户状态
		0 未登录/ 1 已登录
is_delete
	0:删除 1:有效


购物车商品条目模型
id
	主键
cart_id
	外键，购物车id
good_Id
	商品id
good_quantity
	商品数量
flag
	商品状态，是否已购买结算
		0 否 1 已结算
"""