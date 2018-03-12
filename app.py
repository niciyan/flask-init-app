from flask import Flask, render_template, jsonify, redirect, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "dev-key"

class MyForm(FlaskForm):
    number = IntegerField('Size[KB]', validators=[InputRequired("you need put data."), NumberRange(1, 99999999)])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    result = ""
    answer = {}
    if form.validate_on_submit():
        number = form.number.data
        # now = datetime.now().strftime("%Y年%m月%d日 %H:%m:%S")
        # answer['now'] = now
        # answer['number'] = number 
        answer = create_answer(number)
        flash('You put {}.'.format(number))
        return render_template('greet.html',
                form=MyForm(),
                answer=answer
                )
    return render_template('greet.html',
            form=form,
            result=result
            )

@app.route('/greet')
def greet():
    return jsonify({"greeting":"hello"})

def create_answer(number):
    answer = {}
    now = datetime.now().strftime("%Y年%m月%d日 %H:%m:%S")
    answer['now'] = now
    # answer['number'] = number 
    answer['per_min'] = optimize_unit(number * 60)
    answer['per_hour'] = optimize_unit(number * 60 * 60)
    answer['per_day'] = optimize_unit(number * 60 * 60 * 24)
    answer['per_month'] = optimize_unit(number * 60 * 60 * 24 * 30)
    return answer

def optimize_unit(number):
    megabyte = 1000
    gigabyte = 1000 * 1000
    terabyte = 1000 * 1000 * 1000
    if number >= terabyte:
        return "{}[TB]".format(number / terabyte) 
    if number >= gigabyte:
        return "{}[GB]".format(number / gigabyte) 
    if number >= megabyte:
        return "{}[MB]".format(number / megabyte) 

    return "{}[KB]".format(number)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()

