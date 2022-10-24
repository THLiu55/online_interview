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


    if True:
         # 构建CreateInterviewModel模型
        create_interview_model = CreateInterviewModel(user_email=user_email, room_id=1, position=position, date=date, time=time, time_span=time_span, interviewee_name=interviewee_name)
        db.session.add(create_interview_model)
        db.session.commit()
        return render_template("enterroom.html")