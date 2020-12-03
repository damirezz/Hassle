from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2,os
from flask_login import LoginManager                                                                


app= Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = 'c0fbe999bd372d311e4b899a64b3b4f9fc3ee16612664cdbdbab02fe2ad1'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://aocywnwjpijwqz:24fe71b55ad17236411f6e1e12beedfbb1300154a288ebfcc4de7d6fbd11de0b@ec2-3-231-48-230.compute-1.amazonaws.com:5432/d1vk0dsvd6pdpn'
db = SQLAlchemy(app)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
from qanda.idle.routes import idle
from qanda.user.routes import user
from qanda.account.routes import account

app.register_blueprint(idle)
app.register_blueprint(user)
app.register_blueprint(account)