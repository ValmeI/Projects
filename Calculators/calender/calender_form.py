from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class CalenderFrom(FlaskForm):

    beginning_date = DateField('Algus kuupäev',

                               validators=[DataRequired()],
                               format='%Y-%m-%d')

    end_date = DateField('Lõpp kuupäev', validators=[DataRequired()], format='%Y-%m-%d')

    delete_row = SelectField('Sisestatud andmed', choices=[('cpp', 'C++'), ('py', 'Python')])

    submit = SubmitField('Arvuta')


