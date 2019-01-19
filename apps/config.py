import datetime
import os

BASE_DIR = os.path.dirname(__file__)
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'static/upload/')


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
    #    配置session的存储方式
    SESSION_TYPE = 'redis'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)
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
    password = database.get('PASSWORD') or 'zzw12345'
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
        'PASSWORD': 'zzw12345'
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
# flask-sqlacodegen --outfile models.py  --flask mysql+pymysql://root:zzw123@127.0.0.1/tpp
