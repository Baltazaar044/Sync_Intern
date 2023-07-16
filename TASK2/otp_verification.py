import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import math
import random
import re

def generateOTP():
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP +=digits[math.floor(random.random()*10)]
    return OTP     
generated_otp=generateOTP()

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = subject

    # Attach the message to the email
    email_message.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # Start the TLS connection
        smtp.starttls()
        
        # Log in to the email account
        smtp.login(sender_email, sender_password)

        # Send the email
        smtp.send_message(email_message)

# Enter the details
sender_email = 'thisismyprojectspace@gmail.com'
sender_password = 'pthvujfhaofowamd'
recipient_email = 'deepakradhakrishnan044@gmail.com'
subject = 'Test Email'
message = generated_otp
send_email(sender_email, sender_password, recipient_email, subject,message)


def verify_email(email, recipient_email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) and email == recipient_email 

def verify_otp(sent_otp,expected_otp):
    return sent_otp==expected_otp
expected_otp=message

#Enter the recepient email and the OTP rreceived
email = input("Enter your email address: ")
user_otp = input("Enter the OTP: ")

if verify_email(email, email) and verify_otp(user_otp, expected_otp):
    print("Email and OTP verification successful!")
else:
    print("Verification failed. Please check your email and OTP again.")
