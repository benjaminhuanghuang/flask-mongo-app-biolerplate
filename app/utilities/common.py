from flask import current_app
import bleach

def linkify(text):
    text = bleach.clean(text, tags=[], attributes={}, styles=[], strip=True)
    return bleach.linkify(text)


def email(to_email, subject, body_html, body_text):
    # don't run this if we're running a test or setting is False
    if current_app.config.get('TESTING') or not current_app.config.get('AWS_SEND_MAIL'):
        return False

    client = None  # boto3.client('ses')
    return client.send_email(
        Source='webmaster@fromzero.io',
        Destination={
            'ToAddresses': [
                to_email,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': body_html,
                    'Charset': 'UTF-8'
                },
            }
        }
    )
