import smtplib
from email.mime.text import MIMEText

body="This is a test email from python script. how are you"
msg=MIMEText(body)
msg['From']="deepakdm2016@gmail.com"
msg['To']="deepakdm2016@gmail.com"
msg['Subject']="Email from Python"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("deepakdm2016@gmail.com","WinVini@2018")
server.send_message(msg)
print("Mail is sent")

server.quit()