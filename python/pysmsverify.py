'''
import pysmsverify
# Collect number from user
verifier = pysmsverify.SMSVerifier(api_code="YOUR_API_CODE",
                                   message="YOUR MESSAGE",
                                   number="YOUR PHONE NUMBER")
verifier.sendMessage()
# Collect code from user
verifier.verifyCode(INPUTTED_CODE)
'''


import string
import random


# Add Raise Errors
# invalid: number, apikey
# too long, short: apikey, code/ping, message
# failed to send json


class SMSVerify:
    __slots__ = ('api_key',
                 'code',
                 'message',
                 'number')

    def __init__(self,
                 api_key,
                 message,
                 number):
        self.setAPIKey(api_key)
        self.setMessage(message)
        self.setNumber(number)
        self.generateCode()

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

    def _generateCode(self, length):
        if length <= 0 or length > 10:
            return True
            # must be between 1 and 10
            pass
        characters = string.ascii_letters + string.digits
        random_code = ''.join(random.choice(characters) for _ in range(length))
        return random_code.upper()

    def generateCode(self):
        self.code = self._generateCode(length=4)

    def _generatePin(self, length):
        if length <= 0 or length > 10:
            # must be between 1 and 10
            return True
            pass
        min_value = 10**(length - 1)
        max_value = 10**length - 1
        return random.randint(min_value, max_value)

    def generatePin(self):
        self.code = self._generatePin(length=4)

    def setMessage(self, message):
        # check length
        self.message = message

    def sendJSON(self, address, json_block):
        return True
        # send json to address and validate it
        pass

    def sendSMS(self):
        return True
        # create json of message and send it and validate it
        pass

    def verifyCode(self, code):
        return True
        pass

    def setAPIKey(self, api_key):
        if self._validateAPIKey(api_key):
            self.api_key = api_key
        else:
            return False
            # api key invalid
            pass

    def _validateAPIKey(self, api_key):
        return True
        # send json to validate api key and validate it
        pass

    def validateAPIKey(self):
        return self._validateAPIKey(self.api_key)
