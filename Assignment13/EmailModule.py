import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def is_connected():
    try:
        import socket
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def sendmail(UserName, Password, To, Attachment=None, Subject=None, Body=None):
    if not os.path.exists(Attachment):
        return

    filename = Attachment
    To = "marvellousinfosystem@gmail.com" #["myfriend.nichal@gmail.com", "dipakmsonar123@gmail.com", "amol3513@gmail.com"]

    try:
        msg = MIMEMultipart()
        msg['From'] = UserName
        msg['To'] = To#','.join(To)
        msg['Subject'] = Subject

        msg.attach(MIMEText(Body, 'html'))
        attachment = open(filename, "rb")
        info = MIMEBase('application', 'octet-stream')
        info.set_payload(attachment.read())
        encoders.encode_base64(info)
        info.add_header('Content-Disposition', "attachment", filename="%s" % "YogeshNichal.txt")
        msg.attach(info)

        email_text = msg.as_string()

        smpt = smtplib.SMTP("smtp.gmail.com", 587)
        smpt.starttls()
        smpt.login(UserName, Password)
        smpt.sendmail(UserName, To, email_text)
        smpt.quit()
        print("Log file send successfully")

    except Exception as E:
        print(E)