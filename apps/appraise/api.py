from flask_restful import Resource

from apps.appraise.models import Appraise


# todo 增加商品评价功能暂未实现
class AppraiseResource(Resource):
    def get(self):
        appraises = Appraise.query.all()
        return 'haha'
