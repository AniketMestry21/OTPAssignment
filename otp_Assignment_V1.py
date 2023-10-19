import random
from twilio.rest import Client


account_sid = "ACe0d4683dd5306c30be4e7d6cff262748"
auth_token = "ea2555f09aaf8a12ed42aa150aa37980"
twilio_number = "+16185528679"
Mob_No = '+918263829478'

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_sms(Mob_No, otp):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=twilio_number,
        to=phone_number
    )
    print("OTP sent successfully.")

if _name_ == "_main_":
    otp = generate_otp()
    send_otp_via_sms(Mob_No, otp)