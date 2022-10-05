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

# 创建一个app对象
app = Flask(__name__)

# app.config[] 配置 配置项全部放到config里
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
# 配置数据库迁移
# migrate = Migrate(app, db)
# 配置项目蓝图
app.register_blueprint(user_bp)
app.register_blueprint(schedule_bp)

db.create_all(app=app)

# 配置session

app.secret_key = os.getenv("SECRET_KEY", "ewqr9urjewfoifd3")

# 配置LoginManager
login_manager = LoginManager()
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied'

# 要求登录界面未登陆会跳转到以下界面
login_manager.login_view = '/user/login'
login_manager.init_app(app)


# 登录的回调函数
@login_manager.user_loader
def load_user(user_id):
    if User.query.filter_by(user_id=user_id).first() is not None:
        curr_user = User()
        curr_user.user_email = user_id
        return curr_user


@app.errorhandler(ValidationError)
def validation_error(e):
    return jsonify({"code": 400, "message": e.args})


if __name__ == '__main__':
    app.run()
