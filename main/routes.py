from flask import render_template, request, Blueprint, redirect, url_for, send_file, flash

from mysite import db
from mysite.main.sendEmail import sendMessage
from mysite.forms.getContact import ContactForm
from mysite.database.models import Contact, Text
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
	return render_template('home.html')

@main.route("/experience")
	return render_template('experience.html', title='Experience');

@main.route("/research")
	return render_template('research.html', title='Research');
	
@main.route("/code")
def code():
	return render_template('code.html', title=Code Samples)

@main.route("/resume")
def resume():
	return send_file(os.environ.get('RESUME_URI'))
	
@main.route("/contact", methods=['GET', 'POST'])
def contact():
	form=ContactForm()
	if request.method=='POST' and form.validate_on_submit():
		#if email address already exists, add message with the existing user
		sender = Contact.query.filter_by(emailAdd=form.contactEmail.data).first()
		if sender:
			text=Text(content=form.contactText.data, sender_Address=sender.emailAdd)
			new=False
		else:
			contact=Contact(firstName=form.firstName.data, lastName=form.lastName.data, emailAdd=form.contactEmail.data)
			text=Text(content=form.contactText.data, sender_Address=contact.emailAdd)
			new=True
			#only add contact to DB if the email address has not been used before
			db.session.add(contact)
		#add message to DB always
		db.session.add(text)
		db.session.commit()
		sendMessage(form.firstName.data, form.lastName.data, form.contactEmail.data, form.contactText.data, new)
		flash('Message sent!', 'success')
		return redirect(url_for('main.contact'))
	return render_template('contact.html', title='Contact Me', form=form)