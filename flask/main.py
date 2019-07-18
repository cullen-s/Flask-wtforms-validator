from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,PasswordField,RadioField,SelectField,TextField,TextAreaField)
from wtforms import validators
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'

#custom validator for checking if password contains at least one upper-case letter
def containsUpperValidator(form, password):
	x = password.data
	if x.isupper() == True:
		raise ValidationError('must contain at least one lower-case character')

#custom validator for checking if password contains at least one lowwer-case letter
def containsLowwerValidator(form, password):
	b = password.data
	if b.islower() == True:
		raise ValidationError('must contain at least one upper-case character')

#custom validator for checking if entry ends with number
def endsWithNumberValidator(form, password):
	string = password.data

	if string.endswith('0'):
		pass
	elif string.endswith('1'):
		pass
	elif string.endswith('2'):
		pass
	elif string.endswith('3'):
		pass
	elif string.endswith('4'):
		pass
	elif string.endswith('5'):
		pass
	elif string.endswith('6'):
		pass
	elif string.endswith('7'):
		pass
	elif string.endswith('8'):
		pass
	elif string.endswith('9'):
		pass
	else:
		raise ValidationError('must end with a number')


class PasswordForm(FlaskForm):
	username = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', [DataRequired(), EqualTo('confirm'), Length(8), containsUpperValidator, containsLowwerValidator, endsWithNumberValidator])
	confirm = PasswordField('Repeat Password', [DataRequired()])
	submit = SubmitField('submit')

# LongCorrectPasscode2

@app.route('/', methods=['GET', 'POST'])
def index():
	form = PasswordForm()
	if form.validate_on_submit():
		session['username']=form.username.data
		session['password']=form.password.data
		session['confirm']=form.confirm.data
		return redirect(url_for('success'))

	return render_template('index.html', form=form)

@app.route('/success')
def success():
		return render_template('success.html')

if __name__ == '__main__':
	app.run(debug=True)