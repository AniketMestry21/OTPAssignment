import re
import math
import random
import smtplib
from twilio.rest import Client
import sms


# code for validate mobile number
def Validate_Mob_No(Mob_No):
    pattern = re.compile("(0|91)?[-\s]?[6-9]\d{9}")
    return pattern.match(Mob_No)


Mob_No = input("Enter Mobile Number: ")

if Validate_Mob_No(Mob_No):
    print("mobile number is valid")
else:
    print("Please enter valid mobile number")


# code for validate email id
def Validate_Email(email_id):
    pattern = re.compile("[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
    return pattern.match(email_id)


email_id = input("Enter email id: ")

if Validate_Email(email_id):
    print("valid email id")
else:
    print("Please enter valid email id")


# code for generate 6 digit otp
OTP = ""


def Generate_OTP():
    digits = "0123456789"
    length = len(digits)
    otp = ""

    for i in range(6):
        otp += digits[math.floor(random.random() * length)]

    OTP = otp


Generate_OTP()
print(OTP)


# code to send otp to the mobile number
def Send_OTP_Over_Mob_No(Mob_No, OTP):
    client = Client(sms.account_sid, sms.auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is ",
        from_=sms.inputNO,
        to="+91" + str(Mob_No),
    )
    print(Message.body)


Send_OTP_Over_Mob_No(Mob_No, OTP)
