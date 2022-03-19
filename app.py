import json

from flask import Flask, render_template, request, abort
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

from filters import translate_day

app = Flask(__name__)
app.secret_key = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'
DAYS = {
    'mon': [],
    'tue': [],
    'wed': [],
    'thu': [],
    'fri': [],
    'sat': [],
    'sun': []
}


@app.template_filter()
def convert_day(value):
    return translate_day(value)


@app.route('/')
def main():
    return 'Main page'


@app.route('/all')
def all_render():
    return 'All teachers'


@app.route('/goals/<goal>/')
def goals_render(goal):
    return f'Here will be goal {goal}'


@app.route('/profiles/<int:id_teacher>/')
def teacher_render(id_teacher):
    with open('data/teachers.json') as f:
        try:
            teacher = json.load(f)[id_teacher]
        except IndexError:
            return abort(404)
    for day, times in DAYS.items():
        for time, vacant in teacher['free'][day].items():
            if vacant:
                times.append(time)
    return render_template(
        'profile.html',
        teacher=teacher,
        days=DAYS
    )


@app.route('/request/')
def request_render():
    return 'Here will be request'


@app.route('/request_done/')
def request_done_render():
    return 'Request done'


@app.route('/booking/<id_teacher>/<day>/<time>/')
def booking_render(id_teacher, day, time):
    return f'Page for form with {id_teacher}, {day}, {time}'


@app.route('/booking_done/')
def booking_done_render(id_teacher, day, time):
    return f'Page for booking done with'


class OrderForm(FlaskForm):
    name = StringField()
    phone = StringField()


class MyForm(FlaskForm):
    name = StringField('Имя')
    email = StringField('E-mail')
    promo = StringField('Промо-код')
    age = IntegerField('Возраст')
    submit = SubmitField()


@app.route('/form/')
def render_form():
    form = OrderForm()
    return render_template("form.html", form=form)


@app.route('/save/', methods=["GET", "POST"])
def render_save():
    if request.method == 'POST':
        return "Форма отправлена"
    else:
        return "Просто зашли посмотреть"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
