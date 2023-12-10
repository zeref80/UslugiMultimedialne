
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACd6471350570aedf4a62335f7802381f6"
auth_token = "f03fd302e580b033fdb79daa848e2b1d"
verify_sid = "VAb1615fd607c2e30e8b5bd0d4f3b296cd"
verified_number = "+48780063699"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)