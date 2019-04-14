import os
import requests
import json
from smartsms_py.exception import SmartSMSException


class SmartSMS(object):

    def __init__(self, sender_id=None, apix_token=None, msg_type=0, routing=2):
        self.allowed_msg_types = [0, 1, 2, 6]
        self.allowed_routing = [2, 3, 4, 5]
        self.sender_id = None

        if msg_type not in self.allowed_msg_types:
            raise SmartSMSException('Invalid Message Type :help - https://docs.smartsmssolutions.com/docs/parameters')

        if routing not in self.allowed_routing:
            raise SmartSMSException('Invalid Routing Value :help - https://docs.smartsmssolutions.com/docs/parameters')

        if apix_token:
            self.api_token = apix_token
        else:
            apix_token = os.getenv('SMARTSMS_APIX_TOKEN')
            if apix_token:
                self.api_token = apix_token
            else:
                raise SmartSMSException('Missing API_X Token. Set Token in ENV or Pass to Class Constructor.')

        if sender_id:
            self.sender_id = sender_id
        self.msg_type = msg_type
        self.routing = routing
        self.base_url = 'https://smartsmssolutions.com/api/json.php'

    def __call_service(self, url, method='POST', data=None):
        response = None
        if method == 'POST':
            response = requests.post(url=url, data=data, verify=False)

        if method == 'GET':
            response = requests.get(url=url, params=data)

        if response and response.status_code == 200:
            return response.text
        return False

    def send_message(self, recipients, message, sender_id=None, msg_type=0, routing=2, schedule=''):
        if msg_type not in self.allowed_msg_types:
            raise SmartSMSException('Invalid Message Type :help - https://docs.smartsmssolutions.com/docs/parameters')

        if routing not in self.allowed_msg_types:
            raise SmartSMSException('Invalid Routing Value :help - https://docs.smartsmssolutions.com/docs/parameters')

        if sender_id:
            sender = sender_id
        elif self.sender_id:
            sender = self.sender_id
        else:
            raise SmartSMSException('Sender ID Missing. Please Set On method call or class constructor')

        if type(recipients) is list:
            recipients = ','.join(recipients)

        payload = {
            'sender': sender,
            'to': recipients,
            'message': message,
            'type': msg_type,
            'routing': routing,
            'token': self.api_token,
            'schedule': schedule,
        }

        api_response = self.__call_service(self.base_url, 'POST', payload)
        if api_response:
            return json.loads(api_response)
        return None

    def get_balance(self):
        payload = {
            'checkbalance': 1,
            'token': self.api_token
        }
        return self.__call_service(self.base_url, 'GET', payload)
