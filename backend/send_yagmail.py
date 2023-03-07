import yagmail
import os

FROM = os.environ.get('MAIL_SENDER_ADDRESS')
mailpass = os.environ.get('MAIL_PASS')


def send_mail(to, subject, contents=None, attachments=None):
    # set yag instance
    try:
        yag = yagmail.SMTP(FROM, mailpass)
    except Exception as e:
        print('Error setting up Mail Instance')
        print("Exception when trying to login to Email %s\n" % e)

    # Send Message
    try:
        yag.send(to=to,
                 subject=subject,
                 contents=contents,
                 attachments=attachments
                 )
        print(f'Success: sent  mail to {to}')
    except Exception as e:
        print(f'Failed to send Email to {to}')
        print(f'wanted to send {subject=}'
              f'{contents=}'
              f'{FROM=}'
              f'{mailpass=}'
              )
        print("Exception when trying to send Email %s\n" % e)
