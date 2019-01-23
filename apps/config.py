import datetime
import os

import redis

BASE_DIR = os.path.dirname(__file__)
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'static/upload/')

R = redis.Redis(host="127.0.0.1", port=6379, db=6)


# 基础配置
class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # === 文件上传相关配置====
    # 配置文件上传的根目录
    UPLOADS_DEFAULT_DEST = UPLOAD_ROOT_PATH
    # 生成访问图片的路径
    UPLOADS_DEFAULT_URL = '/static/upload/'
    CACHE_TYPE = 'redis'
    #   配置session的存储方式
    # 密钥
    # SECRET_KEY = "secret_key"
    # # 使用redis缓存
    # SESSION_TYPE = 'redis'
    # # 定义前缀
    # SESSION_KEY_PREFIX= 'flask'
    # # 过期时间
    # PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)
    # # SESSION_REDIS = redis.StrictRedis(host="127.0.0.1", port=6379, db=3)
    #     COOKIE
    REMEMBER_COOKIE_NAME = 'session_id'
    # 上传文件的最大长度
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024


# 生成数据库链接
# 'mysql+pymysql://root:zzw123@127.0.0.1:3306/flask_rest?charset=utf8'
def get_db_uri(database):
    engine = database.get('ENGINE') or 'mysql'
    driver = database.get('DRIVER') or 'pymysql'
    user = database.get('USER') or 'root'
    password = database.get('PASSWORD') or '123456'
    host = database.get('HOST') or '127.0.0.1'
    port = database.get('PORT') or '3306'
    db_name = database.get('DB_NAME')
    charset = database.get('CHARSET') or 'utf8'
    return "{}+{}://{}:{}@{}:{}/{}?charset={}".format(engine, driver, user, password, host, port, db_name, charset)


# 开发环境
class DeveloperConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = '123456'
    database = {
        'ENGINE': 'mysql',
        'DB_NAME': '91gou',
        'PASSWORD': '123456'
    }

    # 打印sql语句
    # SQLALCHEMY_ECHO = True
    # 配置数据库链接
    SQLALCHEMY_DATABASE_URI = get_db_uri(database)
    # 缓存配置
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_PASSWORD = ''
    CACHE_REDIS_DB = 1


# 生产环境
class ProductConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = '7d8d82a98fba47a4898f736f4bf466d0'
    database = {
        'ENGINE': 'mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '112.74.42.138',
        'PORT': '3306',
        'DB_NAME': '91gou',
    }

    # 连接池
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_DATABASE_URI = get_db_uri(database)
    #   缓存配置
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_PASSWORD = ''
    CACHE_REDIS_DB = 1


# 开发环境
ENVI_DEFAULT_KEY = ENVI_DEV_KEY = 'default'
ENVI_PRODUCT_KEY = 'product'

environment = {
    ENVI_DEFAULT_KEY: DeveloperConfig,
    ENVI_DEV_KEY: DeveloperConfig,
    ENVI_PRODUCT_KEY: ProductConfig,
}



"""
==============支付宝配置=================
"""
# 支付宝注册应用生成的IP
APP_ID = '2016092300580718'

# 沙箱环境支付网关就是沙箱那面那个关口
PAY_URL_DEV = 'https://openapi.alipaydev.com/gateway.do'
# 正式支付的网关
PAY_URL = 'https://openapi.alipay.com/gateway.do'
# 公钥,私钥
APP_PRIVATE_KEY_STR = open(os.path.join(BASE_DIR, 'alipay/app_private_key.pem')).read()
APP_PUBLICK_KEY_STR = open(os.path.join(BASE_DIR, 'alipay/app_public_key.pem')).read()

"""
==============支付宝配置=================
"""

