import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_addr, sender_pwd, recipient_addr, subject, body):
    FROM = sender_addr
    TO = recipient_addr if isinstance(recipient_addr, list) else [recipient_addr]
    SUBJECT = subject
    TEXT = body
    try:
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    except:
        print('Composing Message Failed')

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()  # optional, called by login()
        server_ssl.login(FROM, sender_pwd)
        server_ssl.sendmail(FROM, TO, message)
        # server_ssl.quit()
        server_ssl.close()
        print(f'Success: sent  mail to {TO}')
    except:
        print(f'Mail to {TO} failed to send')


send_email(sender_addr='chatbot@sommerblut.de',
           sender_pwd='Aellei2022',
           recipient_addr=['aron@petau.net'],
           subject='Hallo',
           body='Ich kann jetzt auch Mails Schreiben\n'
                'Bisher geht nur Text und auch leider keine Sonderzeichen,\n '
                'aber vielleicht reicht das ja erstmal.\n'
                'Liebe Gruesse\n'
                'Aellei'
           )
