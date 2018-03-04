#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import time
import smtplib
from email.mime.text import MIMEText

def sendEmail(title,message,destination):

    fromaddress = 'ringlgamesh@gmail.com'
    toaddress = destination

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('ringlgamesh@gmail.com','Google#9527')

    msg = MIMEText(message)
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Subject'] = (title)

    server.sendmail(fromaddress,toaddress,msg.as_string())
    server.quit

#ID = requests.get('https://www.iyingdi.cn/feed/list/seed/v2?web=1&seed=2&system=web').json().get('feeds')[0].get('feed').get('sourceID')
ID = None

while True: 

    Time = time.localtime()
    
    if Time.tm_sec == 0:

        FEED = requests.get('https://www.iyingdi.cn/feed/list/seed/v2?web=1&seed=2&system=web').json().get('feeds')[0].get('feed')
        tmp = FEED.get('sourceID')

        if tmp != ID:
            title = FEED.get('title')
            description = FEED.get('description')
            mailTitle = '炉石新文章:'+title.encode('utf-8')
            mailContent = description.encode('utf-8')
            sendEmail(mailTitle,mailContent,'582981961@qq.com')
            ID = tmp

    time.sleep(1)
