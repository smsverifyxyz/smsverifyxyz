#import string
#import random
import requests

# Add Raise Errors
# invalid: number
# too long, short: apikey, apitoken
# failed to send dict


class SMSVerify:
    __slots__ = ('api_key',
                 'api_token',
                 'code',
                 'number')

    def __init__(self,
                 api_key,
                 api_token,
                 number):
        self.api_key = api_key
        self.api_token = api_token
        self.number = number

    def _validateNumber(self, number):
        return True
        # only numbers
        # rm +1
        # correct length
        pass

    def validateNumber(self):
        return self._validateNumber(self.number)

    def sendSMS(self):
        self.validateNumber()
        # create dict of message and send it and validate it
        payload = {
            'api_key': self.api_key,
            'api_token': self.api_token,
            'number': self.number
        }
        url = 'https://smsverify.xyz/send.cgi'
        try:
            response = requests.get(url, params=payload)
            if response.status_code == 200:
                return response.text
            else:
                return f"Request failed with status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Request error: {e}"

    def verifyCode(self):
        payload = {
            'api_key': self.api_key,
            'api_token': self.api_token,
            'code': self.code,
            'number': self.number
        }
        url = 'https://smsverify.xyz/code.cgi'
        try:
            response = requests.get(url, params=payload)
            if response.status_code == 200:
                return response.text
            else:
                return f"Request failed with status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Request error: {e}"

