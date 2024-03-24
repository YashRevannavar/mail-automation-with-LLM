from ml.llm import *
from gmail.g_mail import *


def send_email_main(receiver: str):
    response = email_llm_model()
    send_email(subject=response['Subject'],
               body=response['Body'],
               directory_path='./data/attachment/',
               receiver=receiver)
    return None


if __name__ == '__main__':
    print(f"Sending email {EMAIL_RECEIVER}")
    send_email_main(receiver=EMAIL_RECEIVER)
