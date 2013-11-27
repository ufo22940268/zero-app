# coding:utf-8
from flask import Flask, render_template, flash, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, FileField, CameraField, SelectField
from wtforms.validators import Required, InputRequired, Email
import arrow
from eve import Eve
import os.path

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

def create_app(configfile=None):
    THIS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    settings_file = os.path.join(THIS_DIRECTORY, 'settings.py')
    app = Eve(__name__, settings=settings_file)
    #app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
    app.config['WTF_CSRF_ENABLED'] = False

    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/add', methods=['POST', 'GET'])
    def add():
        form = ExampleForm()
        if form.validate_on_submit():
            #ms = int(arrow.now().timestamp)
            #request.files['fileInput1'].save('zero/static/files/%f.jpg' % ms)
            return redirect(url_for('index'))
        return render_template('add.html', form=form)

    return app

def run():
    create_app().run(debug=True)
