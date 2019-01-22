from flask_restful import Resource

from apps.main.field import MainNavFields
from apps.main.models import GoodNav
from apps.utils.response_result import to_response_success, to_response_error


class MainResource(Resource):
    def get(self):
        # good_nav = GoodNav.query.all()
        return 'main'


class MainNavResource(Resource):
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
            return to_response_error()
