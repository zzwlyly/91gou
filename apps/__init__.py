# -*- coding:utf-8 -*-
__author__ = "zzw"
__date__ = "2019/1/19 09:26"

from flask import Flask

from apps.apis import init_api
from apps.config import environment
from apps.ext import init_ext


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(environment.get(env_name))
    init_api(app)
    init_ext(app)
    return app
