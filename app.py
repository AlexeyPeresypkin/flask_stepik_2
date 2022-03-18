from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.secret_key = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'


@app.route('/')
def main():
    return 'Main page'


@app.route('/all')
def all_render():
    return 'All teachers'


@app.route('/goals/<goal>/')
def goals_render(goal):
    return f'Here will be goal {goal}'


@app.route('/profiles/<id_teacher>/')
def teacher_render(id_teacher):
    return render_template('profile.html')
    return f'Here will be teacher {id_teacher}'


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
