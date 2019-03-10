from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, InputRequired
from wtforms.fields.html5 import DateField
from datetime import date


class CalenderFrom(FlaskForm):

    beginning_date = DateField('Algus kuupäev',

                               validators=[DataRequired()],
                               format='%d-%m-%Y')

    end_date = DateField('Lõpp kuupäev', validators=[DataRequired()], format='%d-%m-%Y')

    submit = SubmitField('Arvuta')
