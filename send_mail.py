import smtplib

def send_email():
    sender = "mail"
    password = "password"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        message = input('Enter your message --> ')
        server.login(sender, password)
        server.sendmail(sender, sender, message)
        print('successfully!')
    except Exception as _ex:
        print(f"{_ex}\nCheck your login or password")
    
send_email()
