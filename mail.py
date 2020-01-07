from flask import Flask
from flask_mail import Mail, Message



#import urllib2

# proxy_support = urllib2.ProxyHandler({"http":"http://61.233.25.166:80"})
# opener = urllib2.build_opener(proxy_support)
# urllib2.install_opener(opener)

# html = urllib2.urlopen("http://www.google.com").read()

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your mail address'
app.config['MAIL_PASSWORD'] = 'your mail password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def maill(recp_list,final_msg):
	msg = Message('From easycabpooling', sender ='easycabpooling@gmail.com' , recipients = recp_list)
	msg.body = final_msg
	mail.send(msg)
	return "Sent"


# final_msg="The best match we could find is :  "+space
# 		print("listtttttttttt",recp_list)
# 		msg = Message('you found your partner', sender = 'easycabpooling@gmail.com', recipients = recp_list)
# 		msg.body = final_msg
# 		mail.send(msg)
