#!/usr/bin/env python3

import smtplib

# Function definition

#Function send_using_gemail(user, pwd, recipient, subject, body)
#For sending email using gmail as smtp server
 
#For this to work well go on gmail configure your mail client to use GMail for outgoing mail server.
#Outgoing Mail (SMTP) Server: smtp.gmail.com
#Use Authentication: Yes
#Use Secure Connection: Yes (this can be TLS or SSL depending on your mail client)
#Username: your GMail account, i.e. user@gmail.com
#Password: your GMail password
#Port: 465 or 587

def send_using_gemail(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ("successfully sent the mail")
    except:
        print ("failed to send mail")
		
#Function print_lines_with_prefix(strg, prefx)
#For printing lines in string with a prefix
def print_lines_with_prefix(strg, prefx):	
	for line in strg.split('\n'):
		print (prefx + line);
		
#Now we do some serious business!

#Data Entry
print ()
print ("----------------------------------------------------")
print (" Welcome to Test SMTP")
print ("----------------------------------------------------")
user = input("|-> Enter Your gmail Address: ")
print ();
pswd = input("|-> Enter Your gmail Password: ")
print ();
recipient = input("|-> Enter Recipient email Address: ")


print ();
print ("----------------------------------------------------")
print ("  Confirmation")
print ("----------------------------------------------------")
print ("| Sender Email entered    :" + user)
print ("| Sender Password entered :" + pswd)
print ("| Recipient Email entered :" + recipient)
print ("----------------------------------------------------")

message = """From: From Person <"""+user+""">
To: To Person <"""+recipient+""">
Subject: SMTP e-mail test

This is a test e-mail message.
"""

print ("| Default message to be sent")
print ("----------------------------------------------------")
print_lines_with_prefix(message, "| ")
print ("----------------------------------------------------")

send_using_gemail(user, pswd, recipient, "Test Email", message)