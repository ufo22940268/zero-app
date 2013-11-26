# coding:utf-8
from flask import Flask, render_template, flash, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, FileField, CameraField, SelectField
from wtforms.validators import Required, InputRequired, Email


class ExampleForm(Form):
    field1 = TextField(u'品牌名', validators=[Required()])
    field2 = TextField(u'门店名', validators=[Required()])
    fileInput1 = CameraField(u'图片', description=u'使用系统相机拍照')
    radio_field = SelectField(u'合作类别', choices=[
        ('a', u'优惠'),
        ('b', u'活动'),
        ('c', u'分期'),
    ])
    submit_button = SubmitField(u'提交')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/add', methods=['POST', 'GET'])
    def add():
        form = ExampleForm()
        if form.validate_on_submit():
            return redirect(url_for('index'))
        return render_template('add.html', form=form)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)

def run():
    create_app().run(debug=True)
