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
