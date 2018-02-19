import smtplib
from email.mime.text import MIMEText

fromaddress = 'ringlgamesh@gmail.com'
toaddress = '582981961@qq.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('ringlgamesh@gmail.com','Google#9527')

msg = MIMEText('Main Body')
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = ('Title')

server.sendmail(fromaddress,toaddress,msg.as_string())
server.quit