from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class OrderForm(FlaskForm):
    name = StringField('Ваше имя', [InputRequired()])
    phone = StringField('Ваш телефон', [InputRequired()])
