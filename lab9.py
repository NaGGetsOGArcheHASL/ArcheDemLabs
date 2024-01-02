from flask import Blueprint, render_template

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('lab9/Error.html'), 404


@lab9.route('/lab9/500')
def server_error():
    return render_template("Произошла некоторая ошибка")

@lab9.app_errorhandler(500)
def er500(err):
   return render_template('lab9/500.html'), 500


@lab9.route('/lab9/greeting', methods=['GET', 'POST'])
def greeting():
    class GreetingForm(FlaskForm):
        recipient_name = StringField('Имя получателя', validators=[DataRequired()])
        recipient_gender = SelectField('Пол получателя', choices=[('male', 'Мужской'), ('female', 'Женский')], validators=[DataRequired()])
        sender_name = StringField('Ваше имя', validators=[DataRequired()])
        submit = SubmitField('Отправить')

    form = GreetingForm()

    if form.validate_on_submit():
        recipient_name = form.recipient_name.data
        recipient_gender = form.recipient_gender.data
        sender_name = form.sender_name.data
        return redirect(url_for('lab9.show_greeting', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name))
    return render_template('lab9/greeting.html', form=form)

@lab9.route('/lab9/show_greeting/<recipient_name>/<recipient_gender>/<sender_name>')
def show_greeting(recipient_name, recipient_gender, sender_name):
    return render_template('lab9/show_greeting.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)
