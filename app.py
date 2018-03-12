from flask import Flask, render_template, jsonify, redirect, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, InputRequired

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
    if form.validate_on_submit():
        result = form.name.data
        flash('your name is {}.'.format(result))
        return redirect('/')
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

