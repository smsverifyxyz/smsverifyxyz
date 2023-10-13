import requests
import time

# Add Raise Errors
# invalid: number
# too long, short: apikey, apitoken
# failed to send dict


class SMSVerify:
    __slots__ = ('client_id',
                 'client_secret',
                 'code',
                 'number',
                 'expiration')

    def __init__(self,
                 client_id,
                 client_secret,
                 number):
        self.client_id = client_id
        self.client_secret = client_secret
        self.number = number
        self.expiration = 300

    def setExpirationTime(self, expiration):
        self.expiration = int(time.time()) + int(expiration)

    def _validateNumber(self, number):
        return True
        # only numbers
        # rm +1
        # correct length
        pass

    def validateNumber(self):
        return self._validateNumber(self.number)

    def sendPayload(self, payload):
        url = 'https://smsverify.xyz/relay.cgi'
        try:
            response = requests.get(url, params=payload)
            if response.status_code == 200:
                return response.text
            else:
                return f"Request failed with status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Request error: {e}"

    def sendSMS(self):
        self.validateNumber()
        # create dict of message and send it and validate it
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'number': self.number,
            'expiration': self.expiration
        }
        return self.sendPayload(payload)

    def verifyCode(self):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'number': self.number
        }
        return self.sendPayload(payload)
