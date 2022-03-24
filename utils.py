import json
import random

from models import Teacher


def selected_choose(selected):
    if selected == '0':
        teachers = Teacher.query.all()
        random.shuffle(teachers)
        return teachers
    elif selected == '1':
        teachers = Teacher.query.order_by(Teacher.price.desc()).all()
        return teachers
    elif selected == '2':
        teachers = Teacher.query.order_by(Teacher.price.asc()).all()
        return teachers
    teachers = Teacher.query.order_by(Teacher.rating.desc()).all()
    return teachers


def check_goal(goal):
    with open('data/goals.json') as f:
        data = json.load(f)
        return goal in data


def days_foo(days):
    days_dict = {'mon': [], 'tue': [], 'wed': [], 'thu': [], 'fri': [],
                 'sat': [], 'sun': []}
    for day, times in days_dict.items():
        for time, vacant in days[day].items():
            if vacant:
                times.append(time)
    return days_dict
