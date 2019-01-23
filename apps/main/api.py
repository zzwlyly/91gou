from flask_restful import Resource

from apps.main.field import MainNavFields, MainCategoryFields
from apps.main.models import GoodNav, GoodCategory
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
    分类api
    '''

    def get(self):
        try:
            cates = GoodCategory.query.all()
            return to_response_success(data=cates, fields=MainCategoryFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()
