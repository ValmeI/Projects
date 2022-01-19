from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from Calculators-Website-Flask.work_time import MyFloatField


class WorkForm(FlaskForm):
    pay = IntegerField('Palk',
                       validators=[DataRequired(), NumberRange(min=500)])

    percent = MyFloatField('Protsent',
                           validators=[DataRequired(), NumberRange(0.1, 100)])

    submit = SubmitField('Arvuta')

