from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.secret_key = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'


@app.route('/')
def main():
    pass


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
    app.run(debug=True)
