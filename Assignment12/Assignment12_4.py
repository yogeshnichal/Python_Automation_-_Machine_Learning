import os
import re
import sys
import time
import psutil
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def ProcessDisplay(Dir_name):
    lst = []
    for i in psutil.process_iter():
        lst.append(i.as_dict(attrs=['name', 'pid', 'username']))

    if os.path.isdir(Dir_name) == False:
        os.mkdir(Dir_name, mode=777)

    if os.path.isabs(Dir_name) == False:
        Dir_name = os.path.abspath(Dir_name)

    filename = Dir_name + "\log.txt"
    fd = open(filename, 'w')
    fd.write("Process information ")
    fd.write(time.ctime())

    for i in lst:
        fd.write("\n" + "-" * 80)
        fd.write("\n" + str(i))

    fd.close()

    return filename

def is_connected():
    try:
        import socket
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def send_email(Dir_Path, email_id):
    if is_connected():
        sender = "yogeshnichal@gmail.com"       # enter sender mail id
        receiver = email_id
        data = MIMEMultipart()
        data['From'] = sender
        data['To'] = receiver
        data['Subject'] = "This email sent by program about process log report "

        localtime = time.asctime(time.localtime(time.time()))
        body = "This email script generated on, " + localtime
        data.attach(MIMEText(body, 'plain'))
        filename = "Process_log.txt"
        attachment = open(os.path.abspath(Dir_Path), "rb")

        info = MIMEBase('application', 'octet-stream')
        info.set_payload((attachment).read())
        encoders.encode_base64(info)
        info.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        data.attach(info)

        smpt = smtplib.SMTP('smtp.gmail.com', 587)
        smpt.starttls()
        smpt.login(sender, "gvjdolevefqonlrp")         # enter mail id password
        text = data.as_string()
        smpt.sendmail(sender, receiver, text)
        smpt.quit()
    else:
        print("No internet Connection")


def main():
    print("---------------------------Automation script by Yogesh Nichal---------------------------")
    print("\nApplication name: ", sys.argv[0])
    if (len(sys.argv) != 3):
        print("Application name Directory name Receiver mail id")
        exit()
    try:
        email = sys.argv[2]
        iCnt = 0
        if email:
            iCnt = ProcessDisplay(sys.argv[1])
            if iCnt != 0:
                send_email(iCnt, sys.argv[2])
            else:
                print("Not Able to send email")
        else:
            print("Give proper email_id")
            exit()
    except Exception as E:
        print("Error: Invalid input", E)
    finally:
        print("\n--------------------------------------Thank You--------------------------------------")


if __name__ == "__main__":
    main()