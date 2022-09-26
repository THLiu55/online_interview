import random
import string

from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from forms import LoginFrom, RegisterForm, EmailCaptchaModel, ForgetFormPassword
from flask_login import login_user, logout_user, login_required
from models import User
from exts import db, mail
from flask_mail import Message
from datetime import datetime
from werkzeug.security import generate_password_hash


user_bp = Blueprint("User", __name__, url_prefix="/")

# 登陆界面
@user_bp.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

# 用户登出
@user_bp.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return None

# 注册功能
@user_bp.route("/register", methods=['POST', 'GET'])
def register_check():
    data = request.get_json(silent=True)
    user_email = data["email"]
    user_name = data["userName"]
    user_password = data["password"]
    captcha = data["captcha"]
    register_form = RegisterForm(user_email=user_email, user_name=user_name, user_password=user_password,
                                 captcha=captcha)
    if register_form.validate():
        # 密码md5加密
        hash_password = generate_password_hash(register_form.user_password.data)
        # 构建user模型
        user = User()
        user.user_email = user_email
        user.user_name = user_name
        user.user_password = hash_password
        db.session.add(user)
        db.session.commit()
        return jsonify({"code": 200, "message": "Sign up successfully!"})
    else:
        if register_form.errors.get("user_email"):
            return jsonify({"code":400,"message": "invalidSignUpEmail"})
        elif register_form.errors.get("captcha"):
            return jsonify({"code":400, "message": "invalidSignUpCaptcha"})
        elif register_form.errors.get("user_name"):
            return jsonify({"code":400,"message":"invalidSignUpUserName"})
        else:
            return jsonify({"code":400,"message":"invalidSignUpPassword"})



# 登录功能
@user_bp.route("/login", methods=['POST', 'GET'])
def login_check():
    # 读取json值
    data = request.get_json(silent=True)
    user_email = data["email"]
    user_password = data["password"]
    login_form = LoginFrom(user_email=user_email, user_password=user_password)

    if login_form.validate():
        user = User.query.filter_by(user_email=user_email).first()
        login_user(user)
        return jsonify({"code":200})
    else:
        if login_form.errors.get("user_email"):
            return jsonify({"code": 400, "message": "email"})
        elif login_form.errors.get("user_password"):
            return jsonify({"code": 400, "message": "password"})


# 邮件发送功能
@user_bp.route("/captcha", methods=['POST', 'GET'])
def my_mail():
    data = request.get_json(silent=True)
    email = data['email']
    if email:
        letters = string.ascii_letters + string.digits
        captcha = "".join(random.sample(letters, 6))
        message = Message(
            subject="online_interview 验证码",
            recipients=[email],
            html=render_template("email.html", email_captcha=captcha),
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        # code:200,成功的，正常的请求
        return {'code': 200}
    else:
        # code:400,客户端错误
        return {"code": 400, "message": "请先传递邮箱！"}



# 忘记密码功能-邮箱验证
@user_bp.route("/forget_form_email", methods=['POST', 'GET'])
def email_check():
    data = request.get_json(silent=True)
    email = data["email"]
    captcha = data["captcha"]
    email_model = EmailCaptchaModel.query.filter_by(email=email).first()
    captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
    if email_model:
        if captcha_model.captcha == captcha:
            global the_email
            the_email = email_model.email
            return {"code": 200}
        else:
            return {"code": 400, "message": "captcha"}
    else:
        return {"code": 400, "message": "email"}


# 忘记密码功能-密码更改
@user_bp.route("/forget_form_password", methods=['POST', 'GET'])
def password_check():
    global the_email
    email = the_email
    password_form = ForgetFormPassword(request.form)
    if password_form.validate():
        new_password = password_form.user_password.data
        user_model = User.query.filter_by(user_email=email).first()
        user_model.user_password = generate_password_hash(new_password)
        db.session.commit()
        return redirect(url_for("User.login"))
    else:
        return redirect(url_for("User.login"))

@user_bp.route("/jump/<address>", methods=['GET'])
def jump(address):
    return render_template(address)

