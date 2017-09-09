# from flask import current_app

# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
# from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(subject, recipients, bccs, body_html, body_text, attachment):
    # don't run this if we're running a test or setting is False
    # if current_app.config.get('TESTING'):
    #     return False

    sender = "Benjamin Huang <support@benjamin.com>"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender  # the sender's email address
    msg['To'] = recipients  # the list of all recipients' email addresses
    msg['Bcc'] = bccs

    content_html = MIMEText(body_html, 'html', "utf-8")
    msg.attach(content_html)

    # text_html = MIMEText(body_text, 'html', "utf-8")
    # msg.attach(text_html)

    if attachment:
        body_attach = MIMEApplication(attachment)
        body_attach.add_header('Content-Disposition', 'attachment', filename='attachment-file')
        msg.attach(body_attach)

    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login("afficientatester", "1@11@11@1")
    smtp.sendmail(sender, recipients,"test")
    smtp.quit()


if __name__ == "__main__":
    body_html = "<HTML><BODY><h1>Hello</BODY></HTML>"
    body_text = "Hello"
    subject = "I'am ben"
    recipients = ['huang.huang@afficienta.com', 'benjaminhuanghuang@gmail.com']
    send_email(subject, recipients, None, body_html, body_text, None)
    print("done....")