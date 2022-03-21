import json
import random


def selected_choose(teachers, selected):
    if selected == '0':
        random.shuffle(teachers)
        return teachers
    elif selected == '1':
        return sorted(teachers, key=lambda x: x['price'], reverse=True)
    elif selected == '2':
        return sorted(teachers, key=lambda x: x['price'])
    return sorted(teachers, key=lambda x: x['rating'], reverse=True)


def check_goal(goal):
    with open('data/goals.json') as f:
        data = json.load(f)
        return goal in data
