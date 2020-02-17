import smtplib

def mailer():
    sender = smtplib.SMTP('smtp.gmail.com', 587)
    sender.starttls()
    sender.login("rlaehgud21764011@gmail.com", "08425256@kdh")
    message = "Reigiter Complete"
    sender.sendmail("rlaehgud21764011@gmail.com", "rlaehgud21764011@gmail.com", message)
    sender.quit()


### 실행
mailer()
