from flask_restful import Resource, reqparse

from apps.main.field import MainNavFields, MainCategoryFields, SearchFields, TestMainCateFields
from apps.main.models import GoodNav, GoodCategory
from apps.product.models import Goods
from apps.utils.response_result import to_response_success, to_response_error


class MainNavResource(Resource):
    '''
    导航api
    '''

    def get(self):

        try:
            nav = GoodNav.query.all()

            def get_children(nid=0):
                data = []
                for obj in nav:
                    if obj.parent_id == nid:
                        data.append({"nid": obj.nid, "name": obj.name, "children": get_children(obj.nid)})
                return data

            return to_response_success(data=get_children(), fields=MainNavFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()


class MainCategoryResource(Resource):
    '''
    首页商品api
    '''

    def get(self):
        try:
            cates = GoodCategory.query.all()

            # print(cates[0].name, type(cates[0]))
            # print(dir(cates[0]))
            return to_response_success(data=cates, fields=MainCategoryFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()


class TestMainCategoryResource(Resource):
    '''
    测试数据 首页商品api
    '''

    def get(self):
        try:
            cates = GoodCategory.query.all()

            # print(cates[0].name, type(cates[0]))
            # print(dir(cates[0]))
            return to_response_success(data=cates, fields=TestMainCateFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()


class CategoryResource(Resource):
    '''
    分类api
    '''

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nid', type=int)

    def get(self):
        try:
            nid = self.parser.parse_args().get('nid')
            cate = GoodCategory.query.filter(GoodCategory.nid == nid).first()
            return to_response_success(data=cate, fields=MainCategoryFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()


class SearchResource(Resource):
    '''
    搜索APi
    '''

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('kw', type=str)
        self.parser.add_argument('page', type=int, default=1)
        self.parser.add_argument('size', type=int, default=12)
        super().__init__()

    def get(self):
        parser = self.parser.parse_args()
        kw = parser.get('kw')
        page = parser.get('page')
        size = parser.get('size')
        paginate = Goods.query.filter(Goods.good_desc.like(f'%{kw}%')).paginate(page=page, per_page=size,
                                                                                error_out=False)
        goods = paginate.items

        data = {
            'total': paginate.total,
            'pages': paginate.pages,
            'goods': goods,
        }

        return to_response_success(data=data, fields=SearchFields.result_fields)
