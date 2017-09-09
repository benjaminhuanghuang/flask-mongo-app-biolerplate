from flask import current_app

# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.header import Header
# from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(subject, recipients, bccs, body_html, body_text, attachment=None):
    # don't run this if we're running a test or setting is False
    # if current_app.config.get('TESTING'):
    #     return False

    sender = current_app.config['MAIL_DEFAULT_SENDER'] #"Benjamin Huang <support@benjamin.com>"
    msgAlternative = MIMEMultipart('alternative')
    msgAlternative['Subject'] = Header(subject, 'utf-8')
    msgAlternative['From'] = Header(sender, 'utf-8')  # the sender's email address
    msgAlternative['To'] = Header("my friends", 'utf-8')  # the list of all recipients' email addresses
    msgAlternative['Bcc'] = bccs

    content_text = MIMEText(body_text, 'plain', "utf-8")
    msgAlternative.attach(content_text)
    content_html = MIMEText(body_html, 'html', "utf-8")
    msgAlternative.attach(content_html)



    if attachment:
        body_attach = MIMEApplication(attachment)
        body_attach.add_header('Content-Disposition', 'attachment', filename='attachment-file')
        msgAlternative.attach(body_attach)

    smtp = smtplib.SMTP(current_app.config['MAIL_SERVER'])
    smtp.starttls()
    smtp.login(current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
    smtp.sendmail(sender, recipients, msgAlternative.as_string())
    smtp.quit()


if __name__ == "__main__":
    body_html = "<HTML><BODY><h1>Hello</h1></BODY></HTML>"
    body_text = "The message"
    subject = "The subject"
    recipients = ['huang.huang@afficienta.com', 'benjaminhuanghuang@gmail.com']
    send_email(subject, recipients, None, body_html, body_text, None)
    print("done....")
