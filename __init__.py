from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from mysite.config import Config

db = SQLAlchemy()
mail = Mail()

def create_app():
	#Instantiate a Flask object from the config file
	app = Flask(__name__)
	app.config.from_object(Config)
	
	#initialize database models and Mail object
	db.init_app(app)
	mail.init_app(app)
	
	#Add routes and error handlers to app
	from mysite.main.routes import main
	from cmmwebsite.errors.handlers import errors
	
	app.register_blueprint(main)
	app.register_blueprint(errors)
	
	return app