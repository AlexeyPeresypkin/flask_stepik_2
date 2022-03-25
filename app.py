import random

from flask import Flask, render_template, abort, request
from flask_migrate import Migrate

from filters import translate_day, translate_travel, take_picture
from forms import OrderForm
from models import db, Teacher, Goal, Booking, ApplicationForm
from utils import selected_choose, days_foo

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
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
    teacher = Teacher.query.get_or_404(id_teacher)
    days = teacher.free
    days_with_free_time = days_foo(days)
    return render_template(
        'profile.html',
        teacher=teacher,
        days=days_with_free_time
    )


@app.route('/request/', methods=['GET', 'POST'])
def request_view():
    form = OrderForm()
    goals = Goal.query.all()
    if request.method == 'POST':
        if form.validate_on_submit():
            appform = ApplicationForm(
                name=form.name.data,
                phone=form.phone.data,
                time=request.form.get('time'),
                goal=Goal.query.get_or_404(request.form.get('goal'))
            )
            db.session.add(appform)
            db.session.commit()
            return render_template(
                'request_done.html',
                appform=appform,
            )
    return render_template('request.html', form=form, goals=goals)


@app.route('/booking/<int:id_teacher>/<day>/<time>/', methods=['GET', 'POST'])
def booking_view(id_teacher, day, time):
    form = OrderForm()
    teacher = Teacher.query.get_or_404(id_teacher)
    if request.method == 'POST':
        if form.validate_on_submit():
            time = request.form.get('clientTime')
            day = request.form.get('clientWeekday')
            booking = Booking(
                name=form.name.data,
                phone=form.phone.data,
                time=time,
                day=day,
                teacher=teacher
            )
            db.session.add(booking)
            db.session.commit()
            return render_template(
                'booking_done.html',
                booking=booking
            )
    return render_template(
        'booking.html',
        teacher=teacher,
        day=day,
        time=time,
        form=form
    )


if __name__ == '__main__':
    app.run()
