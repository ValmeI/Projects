from wtforms import FloatField


class MyFloatField(FloatField):
    '# so you could use comma and dot, modifying wtforms FloatField'
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(',', '.'))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid float value'))


class WorkClass:
    def work_calulator(pay, percent):
        default_h = 40
        new_pay = pay * (percent/100)
        new_hours = default_h * (percent/100)
        return new_pay, new_hours

