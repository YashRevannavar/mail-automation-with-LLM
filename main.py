from ml.llm import *
from gmail.g_mail import *

def send_berlin_nova_email(receiver: str):
    response = email_llm_model()
    send_email(subject=response['Subject'],
               body=response['Body'],
               directory_path='./data/attachment/',
               receiver=receiver)
    return None


if __name__ == '__main__':
    print("Sending email to BerlinNova company")
    send_berlin_nova_email(receiver="yashrj13@gmail.com")