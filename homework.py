import time
import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client


load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
NUMBER_FROM = os.getenv('PHONE_NUMBER_FROM')
NUMBER_TO = os.getenv('PHONE_NUMBER_TO')
BASE_URL = os.getenv('URL_VK')
token_vk = os.getenv('TOKEN_VK')
v_api = '5.92'
client = Client(account_sid, auth_token)


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': v_api,
        'fields': 'online',
        'access_token': token_vk,
    }
    return requests.post(BASE_URL,
                         params=params).json()['response'][0]['online']


def send_sms(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO,
    )
    return message.sid


if __name__ == '__main__':
    vk_id = input('Введите id')
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
