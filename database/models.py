from datetime import datetime
from mysite import db

class Contact(db.Model):
	firstName = db.Column(db.String(25), nullable=False)
	lastName = db.Column(db.String(25), nullable=False)
	#email address is unique, it will be used as primary key
	emailAdd = db.Column(db.Text, primary_key=True)
	#messages are stored in Text table
	messages = db.relationship('Text', backref='sender', lazy=True)
	
	def __repr__(self):
		return f"Contact('{self.firstName}', '{self.lastName}', '{self.email}')"

class Text(db.Model):
	#SQLAlchemy autogenerates the id
	id = db.Column(db.Integer, primary_key=True)
	date_received = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	sender_Address = db.Column(db.Text, db.ForeignKey('contact.emailAdd'), nullable=False)
	
	__repr__(self):
		return f"Text('{self.sender_Address}', '{self.content}')"