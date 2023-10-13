import string
import random
import requests

# Add Raise Errors
# invalid: number, apikey
# too long, short: apikey, code/ping, message
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
        self.setAPIKey(api_key)
        self.setAPIToken(api_token)
        self.setNumber(number)

    def _validateNumber(self, number):
        return True
        # only numbers
        # rm +1
        # correct length
        pass

    def validateNumber(self):
        return self._validateNumber(self.number)

    def setNumber(self, number):
        if self._validateNumber(number):
            self.number = number
        else:
            return False
            # not a number
            pass

    def setAPIToken(self, api_token):
        # validate
        self.api_token = api_token

    def sendSMS(self):
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

    def verifyCode(self, code):
        return True
        pass

    def setAPIKey(self, api_key):
        self.api_key = api_key

