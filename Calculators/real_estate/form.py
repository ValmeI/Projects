from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, NumberRange

'My float that it would accept both , and .'
from Calculators.work_time import MyFloatField


class RealEstateFrom(FlaskForm):

    choices = SelectMultipleField('Kinnisvara', choices=[('1', 'Akadeemia tee 42-63'), ('2', 'Akadeemia tee 38-20')])

    price = MyFloatField('Objekti hind',
                         validators=[DataRequired(), NumberRange(min=500)])

    finance = MyFloatField('Sissemakse %',
                           validators=[DataRequired(), NumberRange(0, 100)])

    side_costs = MyFloatField('Kõrvalkulud',
                              validators=[DataRequired(), NumberRange(min=0)])

    rate = MyFloatField('Intress',
                        validators=[DataRequired(), NumberRange(0.1, 100)])

    period = IntegerField('Laenu periood',
                          validators=[DataRequired(), NumberRange(min=1, max=30)])

    rent_per_month = MyFloatField('Kuu rent',
                                  validators=[DataRequired(), NumberRange(0, 5000)])

    insurance = MyFloatField('Kindlustuse makse',
                             validators=[DataRequired(), NumberRange(min=0)])

    m2 = MyFloatField('Korteri m2',
                      validators=[DataRequired(), NumberRange(min=0)])

    submit = SubmitField('Arvuta')
