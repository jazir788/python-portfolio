import smtplib
import ssl
import os

def sendEmail(message):
    host = "smtp.gmail.com"
    port= 465
    username = "jazirtest@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "jazirtest@gmail.com"
<<<<<<< HEAD
=======
    print(username)
    print(password)
>>>>>>> origin/master
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

