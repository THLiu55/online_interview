from flask import Flask, jsonify, app
from wtforms import ValidationError
import config
from flask_login import LoginManager
from flask_migrate import Migrate
from blueprints.user import user_bp
from blueprints.schedule import schedule_bp
from exts import db, mail
import os
from models import User
from flask_cors import CORS


# 创建一个app对象
application = Flask(__name__)

# app.config[] 配置 配置项全部放到config里
application.config.from_object(config)
CORS(application, resources=r'/*')
db.init_app(application)
mail.init_app(application)
# 配置数据库迁移
migrate = Migrate(application, db)
# 配置项目蓝图
application.register_blueprint(user_bp)
application.register_blueprint(schedule_bp)


# 配置session

application.secret_key = os.getenv("SECRET_KEY", "ewqr9urjewfoifd3")

# # 配置LoginManager
# login_manager = LoginManager()
# login_manager.login_message_category = 'info'
# login_manager.login_message = 'Access denied'
#
# # 要求登录界面未登陆会跳转到以下界面
# login_manager.login_view = '/user/login'
# login_manager.init_app(app)
#
#
# # 登录的回调函数
# @login_manager.user_loader
# def load_user(user_id):
#     if User.query.filter_by(user_email=user_id).first() is not None:
#         curr_user = User()
#         curr_user.user_email = user_id
#         return curr_user


if __name__ == '__main__':
    application.run()
