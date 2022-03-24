import json
import random

from dotenv import load_dotenv
from flask import Flask, render_template, abort, request
from flask_migrate import Migrate

from filters import translate_day, translate_travel, take_picture
from forms import OrderForm
from models import db, Teacher, Goal
from utils import selected_choose, days_foo

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
print(app.config.from_object('config.DevelopmentConfig'))
db.init_app(app)
migrate = Migrate(app, db)


@app.template_filter()
def convert_day(value):
    return translate_day(value)


@app.template_filter()
def convert_goal(value):
    return translate_travel(value)


@app.template_filter()
def travel_picture(value):
    return take_picture(value)


@app.route('/')
def main_view():
    teachers = Teacher.query.order_by(Teacher.rating.desc()).limit(6)
    return render_template('index.html', teachers=teachers)


@app.route('/all', methods=['GET', 'POST'])
def all_teachers_view():
    if request.method == 'POST':
        selected = request.form.get('selected')
        teachers_sort = selected_choose(selected)
        return render_template('all.html', teachers=teachers_sort,
                               selected=selected)
    teachers = Teacher.query.all()
    random.shuffle(teachers)
    return render_template('all.html', teachers=teachers, seleted='0')


@app.route('/goals/<goal>/')
def goals_view(goal):
    goal = Goal.query.filter_by(title=goal).first()
    if not goal:
        return abort(404)
    teachers = Teacher.query.filter(Goal.id == goal.id). \
        order_by(Teacher.rating.desc()).all()
    return render_template('goal.html', teachers=teachers, goal=goal.title)


@app.route('/profiles/<int:id_teacher>/')
def teacher_view(id_teacher):
    teacher = Teacher.query.get(id_teacher)
    days = teacher.free
    days_with_free_time = days_foo(days)
    return render_template(
        'profile.html',
        teacher=teacher,
        days=days_with_free_time
    )


@app.route('/request/')
def request_view():
    form = OrderForm()
    with open('data/goals.json') as f:
        goals = json.load(f)
    return render_template('request.html', form=form, goals=goals)


@app.route('/request_done/', methods=['POST'])
def request_done_view():
    print(request.form)
    form = OrderForm()
    time = request.form.get('time')
    goal = request.form.get('goal')
    if form.validate_on_submit():
        with open('data/requests.json') as f:
            data = json.load(f)
        data.append({
            'name': form.name.data,
            'phone': form.phone.data,
            'time': time,
            'goal': goal,
        })
        with open('data/requests.json', 'w') as f:
            json.dump(data, f, indent=4)
    return render_template(
        'request_done.html',
        goal=goal,
        time=time,
        name=form.name.data,
        phone=form.phone.data
    )


@app.route('/booking/<int:id_teacher>/<day>/<time>/')
def booking_view(id_teacher, day, time):
    form = OrderForm()
    with open('data/teachers.json') as f:
        teacher = json.load(f)[id_teacher]
    return render_template(
        'booking.html',
        teacher=teacher,
        day=day,
        time=time,
        form=form
    )


@app.route('/booking_done/', methods=['POST'])
def booking_done_view():
    form = OrderForm()
    time = request.form.get('clientTime')
    day = request.form.get('clientWeekday')
    teacher_id = request.form.get('clientTeacher')
    if form.validate_on_submit():
        with open('data/booking.json') as f:
            data = json.load(f)
        data.append({
            'name': form.name.data,
            'phone': form.phone.data,
            'time': time,
            'day': day,
            'teacher_id': teacher_id,
        })
        with open('data/booking.json', 'w') as f:
            json.dump(data, f, indent=4)
    return render_template(
        'booking_done.html',
        day=day,
        time=time,
        name=form.name.data,
        phone=form.phone.data
    )


if __name__ == '__main__':
    app.run()
