# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf import FlaskForm  # 父類
from wtforms import StringField  # type=input
from wtforms import SubmitField  # type=submit
from flask import render_template
from wtforms.validators import DataRequired, Length, Email # for validation: email form...

app = Flask(__name__)
app.config['SECRET-KEY'] = 'root'


class NameForm(FlaskForm):  # 繼承父類
    name = StringField('name')
    submit = SubmitField('submit')


@app.route('/aa')
def aa():
    form = NameForm
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
