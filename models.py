from exts import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_name = db.Column(db.CHAR(200), nullable=False, unique=False)
    user_password = db.Column(db.CHAR(200), nullable=False)
    user_email = db.Column(db.CHAR(200), primary_key=True, nullable=False, unique=True)

    def get_id(self):
        return self.user_id

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.CHAR(100), nullable=False, unique=True)
    captcha = db.Column(db.CHAR(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class CreateInterviewModel(db.Model):
    __tablename__ = "create_interview"
    position = db.Column(db.CHAR(100),nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)
    time_span = db.Column(db.Integer,nullable=False)
    interviewee_name = db.Column(db.CHAR, nullable=False)
