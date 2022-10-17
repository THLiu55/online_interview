from exts import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_name = db.Column(db.CHAR(200), nullable=False, unique=False)
    user_password = db.Column(db.CHAR(200), nullable=False)
    user_email = db.Column(db.CHAR(200), primary_key=True, nullable=False, unique=True)

    def get_id(self):
        return self.user_email

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.CHAR(100), nullable=False, unique=True)
    captcha = db.Column(db.CHAR(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class CreateInterviewModel(db.Model):
    __tablename__ = "create_interview"
    user_email=db.Column(db.CHAR(200),primary_key=True, default="hhh@qq.com")
    room_id=db.Column(db.Integer,primary_key=True, default=1, autoincrement=True)
    position = db.Column(db.CHAR(100),nullable=False, default="pos")
    date = db.Column(db.DATE, nullable=False, default="yyyy-mm-dd")
    time = db.Column(db.TIME, nullable=False, default="hh:mm:ss")
    time_span = db.Column(db.Integer,nullable=False, default=20)
    interviewee_name = db.Column(db.CHAR(200), nullable=False, default="test")


class Room(db.Model):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    finished = db.Column(db.BOOLEAN, default=False)
    video_address=db.Column(db.CHAR(255))
    white_board=db.Column(db.CHAR(255))
    code_document=db.Column(db.Text())
    close_time=db.Column(db.DateTime, default=datetime.now)