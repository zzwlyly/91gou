from flask_restful import Resource

from apps.main.field import MainNavFields
from apps.main.models import GoodNav
from apps.utils.response_result import to_response_success, RESPONSE_SUCCESS_STATUS


class MainResource(Resource):
    def get(self):
        # good_nav = GoodNav.query.all()
        return 'main'


class MainNavResource(Resource):
    def get(self):

        first_nav = GoodNav.query.filter(GoodNav.level == 1).all()
        second_nav = GoodNav.query.filter(GoodNav.level == 2).all()
        third_nav = GoodNav.query.filter(GoodNav.level == 3).all()
        nav = []
        sec = []
        thi = []
        for first in first_nav:
            nav.append(first)
            for second in second_nav:
                if first.nid == second.parent_id:
                    sec.append(second)
                    nav.append([first, {'second': second}])
                    # for third in third_nav:
                    #     if second.nid == third.parent_id:
                    #         thi.append(third)
                    #         sec.append({'third': thi})

        print(nav)
        # print(first_nav, second_nav, third_nav)

        return to_response_success(data=nav, fields=MainNavFields.result_fields)
        # return 'main'

    def post(self):

        return RESPONSE_SUCCESS_STATUS
