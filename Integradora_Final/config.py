from decouple import config 
class Config:
    SECRET_KEY = '|b2Jqw)h)35LHmKX'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='prueba.crwxcbze5ub7.us-east-1.rds.amazonaws.com'
    MYSQL_USER='user-swal'
    MYSQL_PASSWORD='swaluser$'
    MYSQL_DB='SWAL'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS = True
    MAIL_USERNAME='20213tn148@utez.edu.mx'
    MAIL_PASSWORD='C27EE535771c'
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
#FS/5o3f71KbIPv@]