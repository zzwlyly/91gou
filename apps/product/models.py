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
			.....
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
import datetime

from apps.ext import db

'''
##########good_nav（首页商品分类导航）#########
商品
	good_nav（首页商品分类导航）
		nid
			主键，自增id
				父id
		parent_id      当前类别所属的父id
		name           当前分类名称
			
'''
class good_nav(db.Model):
    nid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    # 分类级别: 1 / 2 / 3
    level=db.Column(db.Integer,nullable=False)
    # 导航排序
    sort=db.Column(db.Integer,nullable=False)
    # 创建时间
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now())
    # 0:删除 1:有效
    is_delete= db.Column(db.BOOLEAN, default=1)


    '''
    # 建立关联查询   uselist默认True:查询一对多的关系/False:查询一对一的关系
    subs = db.relationship('SubCategory', lazy='dynamic', backref='t_cate', uselist=True)
    lazy  select   表示一次性将所有的数据全部加载进内存/立即加载
          dynamic   延迟加载(一对多选用) 先加载主表数据,当我们使用字表相关的数据时,才去执行查询

    '''
# =============================================================================这是分界线
'''
########## good_category（商品分类表）##############

		cid          主键，自增id
		nid          外键，当前分类所属父类别id
		name          分类名称
		is_show       0:隐藏 1:显示
		cate_sort      排序号
		is_delete      0:删除 1:有效
		create_time     创建时间
		
		# 创建外键字段    //创表:小写的类名.ID,字符串形式db.ForeignKey(category.cate_id)
       nid = db.Column(db.Integer, db.ForeignKey(good_nav.nid))
      
       # 创建外键字段   //类名.ID(第二种方式)
       sub_id = db.Column(db.Integer, db.ForeignKey(SubCategory.sub_id, ondelete='CASCADE'))
'''
class good_category(db.Model):
    cid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nid = db.Column(db.Integer, db.ForeignKey(good_nav.nid))
    name = db.Column(db.String(255), index=True, nullable=False)
    # 分类级别: 1 / 2 / 3
    is_show=db.Column(db.Integer,nullable=False)
    # 导航排序
    cate_sort=db.Column(db.Integer,nullable=False)
    # 0:删除 1:有效
    is_delete=db.Column(db.BOOLEAN, default=1)
    # 创建时间
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now())
# =============================================================================这是分界线
'''
#############gc_property（分类属性表）##################
gc_property（分类属性表）
		id
		cid              外键 商品分类id
		name              属性名
		values            属性值
		is_delete         0:删除 1:有效
		create_time       创建时间
'''
class gc_property(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey(good_category.cid))
    name=db.Column(db.String(255),nullable=False)
    values=db.Column(db.String(255),nullable=False)
    # 0:删除 1:有效
    is_delete=db.Column(db.BOOLEAN, default=1)
    # 创建时间
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now())

# =============================================================================这是分界线
'''
##############  goods（商品表） #######################
goods（商品表）
		good_id
			商品id
		cid
			外键，当前商品所属类别id
		shop_id        外键，店铺id
		brand_id       品牌id
		good_name        商品名
		stocks          商品总库存
		good_tips       优惠信息
		is_hot          0(否),1(是) 是否热销产品
		is_new          0,1 是否新品
		is_recom         0,1 是否是推荐产品（recommend
		is_sale          0,1 是否上架
		good_desc        商品描述
		good_status     商品状态 -1:违规 0:未审核 1:已审核
		sale_volume      商品总销量
		sale_time       上架时间
		
'''
#     goods（商品表）
class goods(db.Model):
    good_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey(good_category.cid))
    shop_id = db.Column(db.Integer, db.ForeignKey(gc_property.id))
    brand_id=db.Column(db.Integer, autoincrement=True)
    good_name=db.Column(db.String(255),nullable=False)
    stocks=db.Column(db.Integer)
    good_tips=db.Column(db.String(255),nullable=False)
    is_hot=db.Column(db.Integer)
    is_new=db.Column(db.Integer)
    is_recom=db.Column(db.Integer)
    is_sale=db.Column(db.Integer)
    good_desc=db.Column(db.String(255),nullable=False)
    good_status=db.Column(db.Integer)
    sale_volume=db.Column(db.Integer)
    sale_time= db.Column(db.DATETIME, default=datetime.datetime.now())
    # 0:删除 1:有效
    is_delete= db.Column(db.BOOLEAN, default=1)
    # 创建时间
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now())

# =============================================================================这是分界线
'''
goods_spu（商品SPU表）
		spu_id         主键，自增id
		good_id          外键，对应商品id
		spu_prop1-20       spu属性1
		is_delete         0:删除 1:有效
		create_time       创建时间
'''
class goods_spu(db.Model):
    spu_id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    good_id= db.Column(db.Integer, db.ForeignKey(gc_property.id))
    spu_prop1=db.Column(db.String(255))
    spu_prop2=db.Column(db.String(255))
    spu_prop3=db.Column(db.String(255))
    spu_prop4=db.Column(db.String(255))
    spu_prop5=db.Column(db.String(255))
    spu_prop6=db.Column(db.String(255))
    spu_prop7=db.Column(db.String(255))
    spu_prop8=db.Column(db.String(255))
    spu_prop9=db.Column(db.String(255))
    spu_prop10=db.Column(db.String(255))
    spu_prop11=db.Column(db.String(255))
    spu_prop12=db.Column(db.String(255))
    spu_prop13=db.Column(db.String(255))
    spu_prop14=db.Column(db.String(255))
    spu_prop15=db.Column(db.String(255))
    spu_prop16=db.Column(db.String(255))
    spu_prop17=db.Column(db.String(255))
    spu_prop18=db.Column(db.String(255))
    spu_prop19=db.Column(db.String(255))
    spu_prop20=db.Column(db.String(255))
    # 0:删除 1:有效
    is_delete= db.Column(db.BOOLEAN, default=1)
    # 创建时间
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now())


# =============================================================================这是分界线

'''
##############  goods_sku（商品SKU表）##################
goods_sku（商品SKU表）
		sku_id         主键，自增id
		good_id         外键，对应商品id
		sku_name        商品名
		sku_prop1 -5    sku属性
		original_price     原价
		current_price     现价
		show_img          首页显示的一张图片
		good_imgs     当前型号所有的图片
				        如何存储，数据格式
		good_stock     当前型号商品库存
'''
class goods_sku(db.Model):
    sku_id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    good_id= db.Column(db.Integer, db.ForeignKey(gc_property.id))
    sku_name=db.Column(db.String(255))
    spu_prop1=db.Column(db.String(255))
    spu_prop2=db.Column(db.String(255))
    spu_prop3=db.Column(db.String(255))
    spu_prop4=db.Column(db.String(255))
    spu_prop5=db.Column(db.String(255))
    original_price=db.Column(db.Numeric(10,2))
    current_price=db.Column(db.Numeric(10,2))
    show_img=db.Column(db.String(255))
    good_img=db.Column(db.String(255))
    good_stock=db.Column(db.Integer)
    # 0:删除 1:有效
    is_delete= db.Column(db.BOOLEAN, default=1)
    # 创建时间
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now())