import json

from app import app
from models import db, Teacher, Goal

with app.app_context():
    with open('data/goals.json') as f_g:
        data = json.load(f_g)
        for goal, transl_goal in data.items():
            goal_obj = Goal(title=goal, translate_title=transl_goal)
            db.session.add(goal_obj)
        db.session.commit()
    with open('data/teachers.json') as f:
        data = json.load(f)
        for teacher in data:
            teacher_obj = Teacher(
                id=teacher['id'],
                name=teacher['name'],
                about=teacher['about'],
                rating=teacher['rating'],
                picture=teacher['picture'],
                price=teacher['price'],
                free=teacher['free']
            )
            db.session.add(teacher_obj)
            for goal in teacher['goals']:
                goal_obj = Goal.query.filter_by(title=goal).first()
                teacher_obj.goals.append(goal_obj)
    db.session.commit()
