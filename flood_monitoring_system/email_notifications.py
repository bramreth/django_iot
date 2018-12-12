import smtplib
user = 'kentwaterupdates@gmail.com'
password = 'wghkerzlmhiwuhaj'

def send_email(recipient, message):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, recipient, message)
        server.close()
        print('Email to ' + recipient + " sent")

    except:
        print('Email to ' + recipient + " failed to send")

def build_and_send_email(recipient, alerts):
    message = ""
    message += "Subject: " + recipient.full_name + ", there have been flood alerts in your vicinity\n\n"
    message += recipient.full_name + ",\nThe following flood alerts have been issued for your area:\n\n"
    for alert in alerts["alert_data"]:
        message += alert['flood_area'].label + "\n"
        message += "Severity: " + str(alert["severity_rating"]) + "\n"
        message += alert["severity_message"] + "\n"
        message += str(alert["time"]) + "\n"
        message += alert["message"] + "\n\n"
    message += "- Kent Water Updates"
    print(message)
    send_email(recipient.email, message)

