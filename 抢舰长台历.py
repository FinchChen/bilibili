#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import time
import smtplib
from email.mime.text import MIMEText

URL = 'http://api.live.bilibili.com/activity/v1/NewSpring/redBagExchange'

HEADER = {
    'Cookie':'fts=1508263600; LIVE_BUVID=fe19b73c4d343def4790ad24d7900d82; LIVE_BUVID__ckMd5=06085ba75ced9876; rpdid=ipmliowwwpdoswqixkmpw; pgv_pvi=107897856; sid=law2ttpe; UM_distinctid=160c6868103690-000bd190b4e101-3c604504-1fa400-160c68681042c7; im_notify_type_2892086=0; im_local_unread_2892086=0; im_seqno_2892086=37692; finger=edc6ecda; DedeUserID=2892086; DedeUserID__ckMd5=dd5ed1395cc7afcd; SESSDATA=bfa227a2%2C1520329479%2Cfaf684e1; bili_jct=e44f6191d73d28475a8d81646db76c8a; balh_flv_prefer_ws=; balh_server=https://biliplus.ipcjs.win; BANGUMI_SS_21466_REC=173253; buvid3=4F9CDF71-D9F6-4208-BBED-B0EC0B68347E6793infoc; BANGUMI_SS_21680_REC=183804; BANGUMI_SS_21769_REC=173344; BANGUMI_SS_21755_REC=173173; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1518966149,1519057645,1519067570,1519082276; pgv_si=s1823692800; _dfcaptcha=25164cf960d6de225fcbc0335bcc44cf; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1519126099'
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
    counter = tmp.get('round')

    if counter != ROUND:

        r = requests.post(URL, headers = HEADER, data = PAYLOAD)
        print r.content

        if r.json().get('code') == 0:
            tmp = '完成时间: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n\n' + r.text 
            sendEmail('抢到了',tmp,'582981961@qq.com')

        sendEmail('奖池更新','第 ' + str(counter) + ' 池' + '\n' + '时间: ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min),'582981961@qq.com')

        ROUND = counter
            
    time.sleep(0.5)
