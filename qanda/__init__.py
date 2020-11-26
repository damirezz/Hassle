from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = 'c0fbe999bd372d311e4b899a64b3b4f9fc3ee16612664cdbdbab02fe2ad1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zzqefoxvkrtmlw:2b0676a6937f426fd357fd3d3f1544eb14b1f07e099220705852cc8a7baff5c3@ec2-35-168-77-215.compute-1.amazonaws.com:5432/d5bts8e4lirai8'

db = SQLAlchemy(app)
conn=psycopg2.connect(db)


from qanda.idle.routes import idle
from qanda.user.routes import user
from qanda.account.routes import account

app.register_blueprint(idle)
app.register_blueprint(user)
app.register_blueprint(account)