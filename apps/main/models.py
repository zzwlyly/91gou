'''

独立模块之外的模型

商家店铺
shop_id	店铺id	INT 11	PK	N
uid	店铺所属人id	INT 11		N	店主id，外键user--> uid
shop_name	店名	V 50		N
is_self	是否平台自营	TI		N	0：自营 1：非自营
is_delete	删除标志	TI		N	0：删除 1：有效
create_time	创建时间	DT		N


品牌表
brand_id	品牌id	INT 11	pk	N
brand_name	品牌名称	V 100		N
brand_img	品牌图片	V 150		N
brand_desc	品牌简介	TEXT		N
is_delete	是否删除	TI		N	0：删除  1: 有效
create_time	创建时间	DT		N

首页导航分类
nid	分类导航id	INT 11	PK	N
parent_id	当前属性父类id	INT 11		N	值依赖于主键nid
name	分类属性名	V 100		N
level	分类等级	TI		N	1:一级列表，2:二级，3:三级
sort	导航排序	V 50		N
is_delete	是否删除	TI		N	0：删除  1：有效
create_time	创建时间	DT		N

商品分类
cid	分类id	INT 11	PK	N
nid	从表外键	INT 11		N	导航分类从表主键id
name	当前分类名	V 100		N
brand	分类等级	INT 11		N
is_show	分类是否显示	TI		N	0:隐藏 1:显示
cate_sort	分类排序	INT 11		N
is_delete	是否删除	TI		N	0：删除  1：有效
creat_time	创建时间	DT		N

商品属性表
cid	分类id	INT 11	PK	N
cid	从表外键	INT 11		N	商品分类表主键id
name	属性名	V 255		Y
values	属性值	V 255		Y
is_delete	是否删除	TI		N	0：删除  1：有效
creat_time	创建时间	DT		N


'''

import datetime

from apps.ext import db


