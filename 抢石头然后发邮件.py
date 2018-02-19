#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import time
import smtplib
from email.mime.text import MIMEText

URL = 'http://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'

HEADER = {
    #'Cookie': 'l=v; finger=888236dc; LIVE_BUVID=AUTO7015179513350665; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1517951332; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1517954404; sid=5tk0kq4c; fts=1517951337; buvid3=FF54B876-8A47-4AB1-8653-D64AB9F6549B14056infoc; DedeUserID=2892086; DedeUserID__ckMd5=dd5ed1395cc7afcd; SESSDATA=bfa227a2%2C1520543427%2C97501eda; bili_jct=0ccdc271ddb227fdc184a30bc2409258; _dfcaptcha=0a41f041c15d87059090c345612287cd',
    'Cookie': 'bili_jct=c29d3f8ddab5fb2fbbec2b1b5ec152c5; DedeUserID=56373701; DedeUserID__ckMd5=16f7317c14fdeac1; SESSDATA=42646427%2C1519386700%2C594fd78e; JSESSIONID=931E89C32EE07AED355B617FE5A26999; LIVE_BUVID=3e4530bbb6f7d5ddbf2bf182ce6c4fcf; LIVE_BUVID__ckMd5=557541bbbc2d8f0c; sid=k1ffv3oq'
    }

PAYLOAD = {
    'award_id': 'stuff-1',
    'exchange_num': '10'
    }

def sendEmail(title,message):

    fromaddress = 'ringlgamesh@gmail.com'
    toaddress = '582981961@qq.com'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('ringlgamesh@gmail.com','Google#9527')

    msg = MIMEText(message)
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Subject'] = (title)

    server.sendmail(fromaddress,toaddress,msg.as_string())
    server.quit

#lastROUND = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool?_='+str(time.time())).json().get('data').get('round')

while True: 
    #thisROUND = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool?_='+str(time.time())).json().get('data').get('round')

    Time = time.localtime()

    #if Time.tm_sec % 2 == 0:
        #print 'time: ' + str(Time.tm_hour) + ':' + str(Time.tm_min) + ':' + str(Time.tm_sec) + ' round: ' + str(thisROUND)
    
    if Time.tm_min == 59 and Time.tm_sec >= 55:

        while True: # time.localtime().tm_sec >= 57 or time.localtime().tm_sec <= 2:

            r = requests.post(URL, headers = HEADER, data = PAYLOAD)
            #print r.text "不能加这个因为加了之后很慢"
            if r.json().get('code') == 0:
                tmp = 'Mission Complete at: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n\n' + r.text 
                sendEmail('Success!',tmp)
                break
            
            if time.localtime().tm_sec == 3 or time.localtime().tm_sec == 4:

                tmp = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool').json().get('data').get('pool_list')
                tmp1 = ' '
                
                for i in range (8):
                    
                    '''
                    if  tmp[i].get('award_id') == 'stuff-1':
                        sendEmail('Stone shows up but failed','Check the terminal')
                        break

                    if i == 7:
                        sendEmail('No Stone this time','')
                    '''

                    if tmp[i].get('award_id') == 'stuff-3':
                        tmp1 += ' 贤者之石'
                    elif tmp[i].get('award_id') == 'guard-3':
                        tmp1 += ' 舰长'
                    elif tmp[i].get('award_id') == 'arawd-calendar':
                        tmp1 += ' 台历'

                if tmp1 != ' ':
                    sendEmail('特殊礼物出现了','时间:' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n\n' + '本时段礼物:' + tmp1)

                break

    '''
    if thisROUND != lastROUND:
        r1 = requests.post(URL, headers = HEADER, data = PAYLOAD)
        if r1.json().get('code') == 0:
            tmp = 'Unexpected income at: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n' + r.text 
            sendEmail('Suprise!',tmp)
        #sendEmail('OOOOPS','POOL UPDATED!')
        lastROUND = thisROUND
    '''

    #print 'last round: ' + str(lastROUND)
    time.sleep(0.1)
