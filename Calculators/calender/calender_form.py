from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class CalenderFrom(FlaskForm):

    beginning_date = DateField('Algus kuupäev', validators=[DataRequired()], format='%d-%m-%Y')

    end_date = DateField('Lõpp kuupäev', validators=[DataRequired()], format='%d-%m-%Y')

    submit = SubmitField('Arvuta')
