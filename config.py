# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'interview'
USERNAME = 'root'
PASSWORD = 'Xzy20011224'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'ewqr9urjewfoifd3'

# email config
MAIL_SERVER = "smtp.163.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "online_interview@163.com"
MAIL_PASSWORD = "ZHCNQPPICUDCVPVB"
MAIL_DEFAULT_SENDER = "online_interview@163.com"