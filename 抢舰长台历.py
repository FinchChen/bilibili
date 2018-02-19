#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import time
import smtplib
from email.mime.text import MIMEText

URL = 'http://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'

HEADER = {
    'Cookie': 'l=v; finger=888236dc; LIVE_BUVID=AUTO7015179513350665; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1517951332; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1517954404; sid=5tk0kq4c; fts=1517951337; buvid3=FF54B876-8A47-4AB1-8653-D64AB9F6549B14056infoc; DedeUserID=2892086; DedeUserID__ckMd5=dd5ed1395cc7afcd; SESSDATA=bfa227a2%2C1520543427%2C97501eda; bili_jct=0ccdc271ddb227fdc184a30bc2409258; _dfcaptcha=0a41f041c15d87059090c345612287cd',
    #'Cookie': 'bili_jct=c29d3f8ddab5fb2fbbec2b1b5ec152c5; DedeUserID=56373701; DedeUserID__ckMd5=16f7317c14fdeac1; SESSDATA=42646427%2C1519386700%2C594fd78e; JSESSIONID=931E89C32EE07AED355B617FE5A26999; LIVE_BUVID=3e4530bbb6f7d5ddbf2bf182ce6c4fcf; LIVE_BUVID__ckMd5=557541bbbc2d8f0c; sid=k1ffv3oq'
    }

PAYLOAD = {
    'award_id': 'silver-100',
    'exchange_num': '1'
    }

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

ROUND = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool').json().get('data').get('round')-1

while True: 

    tmp = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool').json().get('data')
    pool = tmp.get('pool_list')
    counter = tmp.get('round')
    #print 1

    if counter != ROUND:

        '''
        r = requests.post(URL, headers = HEADER, data = PAYLOAD)

        if r.json().get('code') == 0:
            tmp = 'Mission Complete at: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n\n' + r.text 
            sendEmail('Success!',tmp,'582981961@qq.com')
        '''
        sendEmail('奖池更新','第 ' + str(counter) + ' 池' + '\n' + '时间: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min),'582981961@qq.com')

        ROUND = counter
            
    #time.sleep(0.5)
