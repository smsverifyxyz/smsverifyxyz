#!/usr/bin/python3

import pysmsverify

verifier = pysmsverify.SMSVerify(api_key="YOUR_API_KEY",
                                 api_token="YOUR_API_TOKEN",
                                 number="PHONE_NUMER")

out = verifier.sendSMS()
print(out)
