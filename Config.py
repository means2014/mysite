import os

class Config:
	#secure secret key
	SECRET_KEY = os.environ.get('SECRET_KEY')
	
	#Config for database, can be any which is supported by SQLALCHEMY
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	#Config for mail server
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')