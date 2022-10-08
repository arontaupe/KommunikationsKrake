import yagmail
import os

FROM = os.environ.get('MAIL_SENDER_ADDRESS')
mailpass = os.environ.get('MAIL_PASS')


def send_mail(TO, subject, contents=None, attachments=None):
    # set yag instance
    try:
        yag = yagmail.SMTP(FROM, mailpass)
    except:
        print('Error setting up Mail Instance')
    # Send Message
    try:
        yag.send(to=TO,
                 subject=subject,
                 contents=contents,
                 attachments=attachments)
        print(f'Success: sent  mail to {TO}')
    except:
        print(f'Failed to send Email to {TO}')
