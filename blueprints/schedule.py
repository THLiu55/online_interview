from flask import Blueprint, request, jsonify, session, render_template
from datetime import datetime

from models import CreateInterviewModel
from exts import db
from forms import ScheduleForm

schedule_bp = Blueprint("schedule", __name__, url_prefix="/")

@schedule_bp.route("/schedule", methods=['POST', 'GET'])
def register_check():
    data = request.get_json(silent=True)
    user_email = session.get('user_email')
    print("session",session.get('user_email'))
    position = data['position']
    date = data['date']
    time = data['time']
    time_span = data["time_span"]
    interviewee_name = data["interviewee_name"]
    # schedule_form = ScheduleForm(user_email=user_email, position=position, date=date, time=time, time_span=time_span,
    #                              interviewee_name=interviewee_name)
    # if schedule_form.validate():
    if True:
         # 构建CreateInterviewModel模型
         create_interview_model = CreateInterviewModel(user_email=user_email, position=position, date=date, time=time, time_span=time_span, interviewee_name=interviewee_name)
         # createInterviewModel.position = position
         # createInterviewModel.date = date
         # createInterviewModel.time = time
         # createInterviewModel.time_span = time_span
         # createInterviewModel.interviewee_name = interviewee_name
         db.session.add(create_interview_model)
         db.session.commit()
         return render_template("enterroom.html")
    # else:
    #     if schedule_form.errors.get("position"):
    #         return jsonify({"code":400,"message": "invalidPosition"})
    #     elif schedule_form.errors.get("date"):
    #         return jsonify({"code":400, "message": "invalidDate"})
    #     elif schedule_form.errors.get("time"):
    #         return jsonify({"code":400,"message":"invalidTime"})
    #     elif schedule_form.errors.get("time_span"):
    #         return jsonify({"code":400,"message":"invalidTime_span"})
    #     else:
    #         return jsonify({"code":400,"message":"invalidInterviewee_name"})