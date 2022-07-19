import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from termcolor import colored
from secrets import token_hex

# copy-d it to C:\Users\YOURUSER\AppData\Local\Programs\Python\PythonXX-XX\Lib\site-packages


def send_email(stmp_variable, user, password_file, sent_from, sent_to, sent_subject, sent_body):

    server = smtplib.SMTP_SSL(stmp_variable, 465)
    '# get password form file, read only'
    open_file = open(password_file + ".txt", 'r')
    # creates random ID for message-ID, for some reason gmail wants it
    random_id = token_hex(16)

    for password in open_file:

        server.login(user, password)

        msg = EmailMessage()
        msg['From'] = sent_from
        msg['To'] = sent_to
        msg['Subject'] = sent_subject
        msg['Message-ID'] = make_msgid(idstring=random_id)
        msg.set_type('text/html')
        msg.set_content(sent_body)

        server.send_message(msg)
        print(colored('\nMail Send Successfully', 'green'))
        server.quit()

'''
send_email(stmp_variable='valme.noip.me',
           user='email',
           password_file=r'D:\PycharmProjects\Projects\My_Send_Email\synology_pass',
           sent_from='email@valme.noip.me',
           sent_to='ignarvalme@gmail.com',
           sent_subject='Portfelli seis: ',
           sent_body='Tulemus')
'''