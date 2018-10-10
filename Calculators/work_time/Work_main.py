from flask import Flask, render_template, flash
from Calculators.work_time.forms import WorkForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def index():
    return "This is test"


@app.route('/work', methods=['GET', 'POST'])
def work():
    form = WorkForm('''csrf_enabled=False''')
    '''if form.validate_on_submit():
        flash('Tulemus:', 'success')
    else:
        flash('sdasdasdasd', 'danger')
'''

    print(form.errors)
    if form.is_submitted():
        print("submitted")
    if form.validate():
        print("valid")
    if form.validate_on_submit():
        flash("Successfully created a new book")
    return render_template("worktime.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)





