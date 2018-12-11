import smtplib
user = 'kentwaterupdates@gmail.com'
password = 'wghkerzlmhiwuhaj'

def send_email(recipient, subject, text):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server.sendmail(user, recipient, message)
        server.close()
        print("sent")
    except:
        print('Email to ')

send_email("m.taubert2015@gmail.com", "Subject: Email Test", "Testing automated email sending\n\n\nLove,\nMax")