from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, InputRequired
from wtforms.fields.html5 import DateField


class CalenderFrom(FlaskForm):

    beginning_date = DateField('Algus kuupäev',

                               validators=[DataRequired()],
                               format='%Y-%m-%d')

    end_date = DateField('Lõpp kuupäev', validators=[DataRequired()], format='%Y-%m-%d')

    submit = SubmitField('Arvuta')
