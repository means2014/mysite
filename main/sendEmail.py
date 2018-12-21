from datetime import datetime
from flask_mail import Message
from mysite import mail

def sendMessage(firstname, lastname, address, content, newContact=True):
	if newContact:
		msg=Message("New contact from your website!", sender=("Website Contact", "{address}"), recipients=[os.environ.get('EMAIL_ADDRESS')])
	else:
		msg=Message("Returning contact from your website!", sender=("Website Contact", "{address}"), recipients=[os.environ.get('EMAIL_ADDRESS')])
	msg.body=f"{firstname} {lastname} <{address}> sent the following message at {datetime.utcnow()} (UTC): \r\n\r\n {content}"
	
	mail.send(msg)
	return