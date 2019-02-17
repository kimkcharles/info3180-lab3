from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 't00muc4'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '63107dcc396033'
app.config['MAIL_PASSWORD'] = '57708637782c99'

mail = Mail(app)
from app import views