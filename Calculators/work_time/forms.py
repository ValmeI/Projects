from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class WorkForm(FlaskForm):
    pay = IntegerField('Palk',
                       validators=[DataRequired()])

    percent = IntegerField('Protsent',
                           validators=[DataRequired()])

    hours = IntegerField('Töötunde',
                         validators=[DataRequired()])

    submit = SubmitField('Arvuta')

