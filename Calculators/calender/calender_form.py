from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class CalenderFrom(FlaskForm):

    beginning_date = DateField('Algus kuupäev',
                               validators=[DataRequired()],
                               format='%Y-%m-%d')

    end_date = DateField('Lõpp kuupäev', validators=[DataRequired()], format='%Y-%m-%d')

    submit = SubmitField('Lisa')


class CalenderFromDelete(FlaskForm):

    delete_row = SelectField('Select what row to delete', choices=[])

    delete = SubmitField('Delete')
