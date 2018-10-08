from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class WorkForm(FlaskForm):
    pay = IntegerField('Palk',
                       validators=[DataRequired(), NumberRange(0, 100)])

    percent = IntegerField('Protsent',
                           validators=[DataRequired, NumberRange(0, 100)])

    hours = IntegerField('Töötunde',
                         validators=[DataRequired(), NumberRange(0, 60)])

    submit = SubmitField('Arvuta')

