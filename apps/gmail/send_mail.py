# -*- coding: utf-8 -*-
# gamil package{__init__.py, send_mail.py}
# send_mail.py
from flask import render_template
from flask_mail import Message
from threading import Thread
from apps import mail, create_app

app = create_app()

import os

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_SENDER'] = 'email_account'  # os.environ.get('MAIL_USERNAME') 可使用environment value 獲取
# app.config['MAIL_USERNAME'] = 'email_account'  # os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = 'password'  # os.environ.get('MAIL_PASSWORD')


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def senmail(subject, to, txt, number):
    msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = txt
    msg.html = f"<b>{number}</b>"
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

