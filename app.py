from flask import Flask, render_template, jsonify, redirect, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "dev-key"

class MyForm(FlaskForm):
    name = StringField('name', validators=[
        InputRequired()])
    number = IntegerField('number', validators=[InputRequired("you need put data."), NumberRange(1, 100)])
    date = DateField('date', validators=[InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    result = ""
    answer = {}
    if form.validate_on_submit():
        result = form.name.data
        now = datetime.now()
        flash('your name is {}. Now:{}'.format(result, now))
        answer['now'] = now
        answer['x1000'] = number * 1000
        answer = ['x1000000'] = number * 1000 * 1000
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

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()

