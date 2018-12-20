import os

class Config:
	#secure secret key
	SECRET_KEY = os.environ.get('SECRET_KEY')
	
	#Config for database, can be any which is supported by SQLALCHEMY
	SQLALCHEMY_DATABASE_URI = os.environ.get()
	SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get()
	
	#Config for mail server
	MAIL_SERVER = os.environ.get()
	MAIL_PORT = os.environ.get()
	MAIL_USE_TLS = os.environ.get()
	MAIL_USERNAME = os.environ.get()
	MAIL_PASSWORD = os.environ.get()