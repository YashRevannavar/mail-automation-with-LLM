from extras.constants import *
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def send_email(subject: str, body: str, directory_path: str, receiver: str) -> None:
    """
    Send an email with attachments from a specified directory using smtplib and ssl.
    :param subject: The subject of the email
    :param body: The body of the email
    :param directory_path: The path to the directory containing files to be attached
    :param receiver: The email address of the receiver
    """
    email_object = MIMEMultipart()
    email_object['From'] = EMAIL_SENDER
    email_object['To'] = receiver
    email_object['Subject'] = subject
    email_object.attach(MIMEText(body, 'plain'))
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {os.path.basename(filepath)}',
            )
            email_object.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(email_object)
    return print("Email sent successfully!")
