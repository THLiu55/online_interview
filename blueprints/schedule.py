from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from models import CreateInterviewModel, User, Room
from exts import db


schedule_bp = Blueprint("schedule", __name__, url_prefix="/schedule")


@schedule_bp.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == "GET":
        user = User.query.filter_by(user_email=session['user_email']).first()
        interviews = CreateInterviewModel.query.filter_by(user_email=session['user_email']).all()
        return render_template("schedule.html", username=user.user_name, interviews=interviews)
    else:
        pos = request.form.get("pos")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("time")
        span = request.form.get("time_span")
        iname = request.form.get("iname")
        create_interview_model = CreateInterviewModel()
        create_interview_model.user_email = email
        create_interview_model.interviewee_name = iname
        create_interview_model.date = date
        create_interview_model.time = time
        create_interview_model.time_span = span
        create_interview_model.position = pos
        db.session.add(create_interview_model)
        db.session.commit()

        room = Room()
        room.finished = 0
        db.session.add(room)
        db.session.commit()
        return redirect(url_for("schedule.create"))


@schedule_bp.route("/total_interview", methods=['GET'])
def get_total_interview():
    total_interview = len(CreateInterviewModel.query.filter_by().all())
    return jsonify({'total_interview': total_interview}), 200


@schedule_bp.route("/per_interview")
def get_per_interview():
    per_interview = CreateInterviewModel.query.all()
    data = []
    for i in per_interview:
        dict = {
            "position": i.position,
            "date": i.date,
            "time": i.time,
            "time_span": i.time_span,
            "interviewee_name": i.interviewee_name
        }
        data.append(dict)
    return jsonify({"code": 200, "data": data})
