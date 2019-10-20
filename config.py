class Config(object):
    DEBUG = True
    STATIC_URL = '/static'
    SQLALCHEMY_DATABASE_URI = 'postgresql://gatcopressuser:123456@localhost:5432/gatcopress'
    AUTH_LOGIN_ENDPOINT = 'login'
    AUTH_PASSWORD_HASH = 'bcrypt'
    AUTH_PASSWORD_SALT = 'add_salt'
    SESSION_COOKIE_SALT = 'salt_key'
    SECRET_KEY = 'acndefhskrmsdfssadasgs'
    # session
    # SESSION_COOKIE_DOMAIN = '.upstart.vn'
    #SESSION_REDIS_URI = "redis://localhost:6379/9"
