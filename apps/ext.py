from flask_admin import Admin
from flask_cors import CORS
from flask_session import Session
from flask_uploads import UploadSet, IMAGES, DOCUMENTS, configure_uploads
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_caching import Cache


# 初始化第三方插件
def init_ext(app):
    # 初始化数据库
    init_db(app)
    # 初始化登录模块
    init_login(app)
    # 初始化缓存
    init_caching(app)
    # 初始化文件上传
    init_upload(app)
    # 初始化跨域请求
    init_cors(app)
    # 初始化session缓存
    init_session(app)
    # 初始化admin
    init_admin(app)


db = SQLAlchemy()
migrate = Migrate()


# 初始化数据库
def init_db(app):
    db.init_app(app)
    migrate.init_app(app=app, db=db)


se = Session()


# 初始化session缓存
def init_session(app):
    se.init_app(app)


# 实例化登录对象
login_manager = LoginManager()


def init_login(app: Flask):
    login_manager.login_view = '/user/login/'
    # basic   strong  None
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)


# 其他配置
"""
session 存储的位置
# cookie 相关配置
"""

cache = Cache()

"""
pip install redis
CACHE_DEFAULT_TIMEOUT 连接redis超时时间
CACHE_KEY_PREFIX     redis缓存key的前缀
CACHE_REDIS_HOST       ip
CACHE_REDIS_PORT       端口
CACHE_REDIS_PASSWORD   密码
CACHE_REDIS_DB         redis数据库的索引号
CACHE_REDIS_URL        使用url连接地址的方式配置连接数据
"""


def init_caching(app: Flask):
    cache.init_app(app)


"""
文件上传配置
pip install flask-uploads
"""

"""
post请求 form-data
UploadSet 文件上传的核心对象
"""

# media
"""
name 上传文件的子目录 默认是files  
extensions  上传文件的类型(扩展名),默认是 TEXT + DOCUMENTS + IMAGES + DATA
default_dest 配置文件上传的根目录 例如D:\work\PycharmProjects\1805\flask_cache\apps\media
"""
# 上传图片
img_set = UploadSet(name='images', extensions=IMAGES)
# 上传文档文件
doc_set = UploadSet(name='doc', extensions=DOCUMENTS)

"""
 config_uploads 初始化UploadSet对象
"""


def init_upload(app: Flask):
    # 初始化img_set
    configure_uploads(app, img_set)
    # patch_request_class(app,size=32 * 1024 * 1024)
    configure_uploads(app, doc_set)


# 解决前后端跨域请求问题
cors = CORS(resources={r"/api/*": {"origins": "*"}})


def init_cors(app):
    cors.init_app(app)


"""
#######################后台管理################################
"""
from flask_babel import Babel

# 初始化admin
admin = Admin(name="91gou商城后台管理")
babel = Babel()


#
#
def init_admin(app):
    admin.init_app(app)
    babel.init_app(app)


"""
#######################后台管理################################
"""
