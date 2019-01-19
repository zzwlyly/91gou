'''
订单模型

订单
	orders（订单表）
		id
			主键
		oid
			订单号
				唯一
		uid
			用户id
		aid
			收货人id
		status
			-3:用户拒收 -2:未付款的订单 -1：用户取消 0:待发货 1:配送中 2:用户确认收货
		total_money
			订单总金额
		real_money
			实际支付金额
		pay_type
			支付方式
				在线支付/货到付款
		pay_from
			支付来源
				1 支付宝/2 微信/ 3  现金 pos机
		pay_status
			支付状态
				0:未支付 1:已支付
		order_score
			订单成功所获取积分
		remarks
			订单备注
		is_refund
			是否退款
				0:否 1：是
		is_return
			是否退货
				0:否 1：是
					退货是指，商家退款，客户不用退货。客户已退货，商家退款
		is_appraise
			是否评价
				0:未点评 1:已点评
		is_closed
			订单是否完结
				0：未完结 1:已完结
		create_time
			订单创建时间
		pay_time
			订单支付时间
		is_delete
			0:删除 1:有效
	order_item（订单内商品条目表）
		id
			主键
		oid
			外键，订单号
				唯一
		uid
			用户id
				购买的用户
		good_id
			所购买的商品id
		good_quantity
			商品数量
	order_refunds（订单退款退货表）
		id
			主键
		oid
			外键，订单id
		uid
			退款人id
		good_id
			退款商品id
		refund_no
			退款流水号
		refund_remark
			退款备注
		refund_time
			退款时间
		refund_reason
			退款原因
		refund_money
			退款金额
		shop_reason
			商家拒绝退款原因
		refund_status
			退款状态
				-1退款失败 / 0 审核中 / 1 退款成功
		create_time
			退款时间
'''