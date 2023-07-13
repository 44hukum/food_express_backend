import os
from twilio.rest import Client


def send_otp(verified_number):
    account_sid = "AC33e5b5418e0424299a496dccfee23bbd"
    auth_token = "ff598690bd3ed4e99aa767439cafbfb8"
    verify_sid = "VA4fe7a5a76765d28b49eb8c8bacfedd16"

    client = Client(account_sid, auth_token)

    verification = client.verify.v2.services(verify_sid).verifications.create(to=verified_number, custom_friendly_name="Nepalgunj Food otp: ", channel="sms")
    print(verification.status)

    otp_code = input("Please enter the OTP:")


    verification_check = client.verify.v2.services(verify_sid).verification_checks.create(to=verified_number, code=otp_code)
    return verification_check.status

print(send_otp('+9779803251923'))