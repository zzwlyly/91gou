'''
商品

商品
	good_nav（首页商品分类导航）
		nid
			主键，自增id
				父id
		parent_id
			当前类别所属的父id
		name
			当前分类名称
		level
			分类级别
				1/2/3
		sort
			导航排序
		is_delete
			0:删除 1:有效
		create_time
			创建时间
	good_category（商品分类表）
		cid
			主键，自增id
		nid
			外键，当前分类所属父类别id
		name
			分类名称
		is_show
			0:隐藏 1:显示
		cate_sort
			排序号
		is_delete
			0:删除 1:有效
		create_time
			创建时间
	gc_property（分类属性表）
		id
		cid
			主键 商品分类id
		name
			属性名
		values
			属性值
		is_delete
			0:删除 1:有效
		create_time
			创建时间
	goods（商品表）
		good_id
			商品id
		cid
			外键，当前商品所属类别id
		shop_id
			外键，店铺id
		brand_id
			品牌id
		good_name
			商品名
		stocks
			商品总库存
		good_tips
			优惠信息
		is_hot
			0,1 是否热销产品
				0:否 1:是
		is_new
			0,1 是否新品
		is_recom
			0,1 是否是推荐产品（recommend
		is_sale
			0,1 是否上架
		good_desc
			商品描述
		good_status
			商品状态
				-1:违规 0:未审核 1:已审核
		sale_volume
			商品总销量
		sale_time
			上架时间
		is_delete
			0:删除 1:有效
		create_time
			创建时间
	goods_spu（商品SPU表）
		spu_id
			主键，自增id
		good_id
			外键，对应商品id
		spu_prop1
			spu属性1
		spu_prop2
		spu_prop3
		spu_prop4
		spu_prop5
		spu_prop6
		spu_prop7
		spu_prop8
		spu_prop9
		spu_prop10
		spu_prop11
		spu_prop12
		spu_prop13
		spu_prop14
		spu_prop15
		spu_prop16
		spu_prop17
		spu_prop18
		spu_prop19
		spu_prop20
		is_delete
			0:删除 1:有效
		create_time
			创建时间
	goods_sku（商品SKU表）
		sku_id
			主键，自增id
		good_id
			外键，对应商品id
		sku_name
			商品名
		sku_prop1
			sku属性
		sku_prop2
		sku_prop3
		sku_prop4
		sku_prop5
		original_price
			原价
		current_price
			现价
		show_img
			首页显示的一张图片
		good_imgs
			当前型号所有的图片
				如何存储，数据格式
		good_stock
			当前型号商品库存
		is_delete
			0:删除 1:有效
		create_time
			创建时间

'''
