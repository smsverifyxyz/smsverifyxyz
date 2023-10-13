#!/usr/bin/python3

import smsverify
import json

import time

verifier = smsverify.SMSVerify(client_id="YOUR_API_ID",
                               client_secret="YOUR_API_SECRET",
                               number="+1(817)-557 7718")
                               #number="PHONE_NUMER")
expiration = 20
verifier.setExpirationTime(expiration)

out = verifier.sendSMS()
print(out)

#verifier.code = json.loads(out.replace("'", "\""))['code']

#time.sleep(expiration)
#out = verifier.verifyCode()
#print(out)
