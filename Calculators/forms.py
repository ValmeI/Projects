from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


class WorkForm(FlaskForm):
    pay = IntegerField('Palk',
                       validators=[DataRequired(), NumberRange(min=500)])

    percent = FloatField('Protsent',
                         validators=[DataRequired(), NumberRange(0.1, 100)])

    submit = SubmitField('Arvuta')

