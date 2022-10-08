import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yagmail
import keyring

yagmail.register('chatbot@sommerblut.de', 'Aellei2022')
yag = yagmail.SMTP('chatbot@sommerblut.de')


def send_email(sender_addr, sender_pwd, recipient_addr, subject, txt_body, html=None):
    TO = recipient_addr
    # Compose Message

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_addr
    message["To"] = TO
    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    text = MIMEText(txt_body, "plain")
    appendix = MIMEText(html, "html")
    # message.attach(text)
    message.attach(appendix)

    # Send Message

    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo()
    server_ssl.login(sender_addr, sender_pwd)
    server_ssl.sendmail(sender_addr, TO, message.as_string())
    server_ssl.close()
    print(f'Success: sent  mail to {TO}')


send_email(sender_addr='chatbot@sommerblut.de',
           sender_pwd='Aellei2022',
           recipient_addr='aron@petau.net',
           subject='Hallo',
           txt_body='Ich kann jetzt auch Mails \n'
                    'Bisher geht nur Text und auch leider keine Sonderzeichen,\n '
                    'aber vielleicht reicht das ja erstmal.\n'
                    'Liebe Gruesse\n'
                    'Aellei',
           html="""<html>
  <body>
    <p>Hi,<br>
       Check out the new post on the Mailtrap blog:</p>
    <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p>
    <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
  </body>
</html>
"""
           )
