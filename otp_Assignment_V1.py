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
    send_otp_via_sms(Mob_No, otp)import random
import re
import smtplib
from twilio.rest import Client


account_sid = "AC5e2c13017a36a96c62529e24281cf9f1"
auth_token = "50d82397d702b678b5fed876374279a7"
twilio_number = "+13233067978"
# target_number = '+918623043699'


def generate_otp():
    return str(random.randint(100000, 999999))


target_number = input("Enter your mobile number: ")


def send_otp_via_sms(phone_number, otp):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is: {otp}", from_=twilio_number, to=phone_number
    )
    print("OTP sent successfully on your mobile number.")


def is_valid_mobile_number(target_number):
    pattern = r"^\+[0-9]+([- ]?[0-9]+)+$"

    if re.match(pattern, target_number):
        return True
    else:
        return False


if is_valid_mobile_number(target_number):
    otp = generate_otp()
    send_otp_via_sms(target_number, otp)
else:
    print(f"{target_number} is not a valid mobile number.")

# if _name_ == "_main_":
#     otp = generate_otp()
#     send_otp_via_sms(target_number, otp)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

password = "rblp vqku bmle jvrm"
server.login("aniketmestry2104@gmail.com", password)

otp = generate_otp()

receiver_email = input("Enter E-mail ID: ")


def send_otp_via_email():
    sender_email = "aniketmestry2104@gmail.com"
    # receiver_email = 'aniketmestry210@gmail.com'
    message = f"Subject: Your OTP\n\nYour OTP is: {otp}"
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

    print("OTP Sent successfully on your Email.")


# validating email address
def is_valid_email(receiver_email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, receiver_email):
        return True
    else:
        return False


if is_valid_email(receiver_email):
    send_otp_via_email()
else:
    print(f"{receiver_email} is not a valid email address.")
