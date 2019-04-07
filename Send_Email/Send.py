import smtplib
from email.message import EmailMessage
from termcolor import colored


def send_email(stmp_variable, user, password_file, sent_from, sent_to, sent_subject, sent_body):

    server = smtplib.SMTP_SSL(stmp_variable, 465)
    '# get password form file, read only'
    open_file = open(password_file + ".txt", 'r')
    for password in open_file:

        server.login(user, password)

        msg = EmailMessage()
        msg['From'] = sent_from
        msg['To'] = sent_to
        msg['Subject'] = sent_subject
        msg.set_type('text/html')
        msg.set_content(sent_body)

        server.send_message(msg)

        print(colored('\nMail Send Successfully', 'green'))
        server.quit()


''' Testing gmail sending'
Variables are: STMP, username, password file, send from, send to, email title and email body'''
'''
send_email('smtp.gmail.com', 
           'ignarvalme', 
           'gmail_pass', 
           'email@valme.noip.me', 
           'ignarvalme@gmail.com', 
           'test', 
           'body')
'''

'''
Testing synolog local mail servers sending
Variables are: STMP, username, password file, send from, send to, email title and email body
'''
'''
send_email('valme.noip.me',
           'email',
           'synology_pass',
           'email@valme.noip.me',
           'ignarvalme@gmail.com',
           'test',
           'body')
'''

