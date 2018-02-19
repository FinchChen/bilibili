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

ROUND = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool').json().get('data').get('round')-1

while True: 

    Time = time.localtime()
    
    if Time.tm_sec == 0:

        tmp = requests.get('http://api.live.bilibili.com/activity/v1/NewSpring/redBagPool').json().get('data')
        pool = tmp.get('pool_list')
        counter = tmp.get('round')
        giftList = ''
        tmp1 = ' '

        if counter != ROUND:
                    
            for i in range (8):

                if pool[i].get('award_id') == 'stuff-1':
                    giftList += '经验原石 '
                elif pool[i].get('award_id') == 'stuff-2':
                    giftList += '经验曜石 '
                elif pool[i].get('award_id') == 'stuff-3':
                    giftList += '贤者之石 '
                elif pool[i].get('award_id') == 'award-master':
                    giftList += '推荐位 '
                elif pool[i].get('award_id') == 'gift-113':
                    giftList += '新春抽奖 '
                elif pool[i].get('award_id') == 'silver-100':
                    giftList += '银瓜子 '
                elif pool[i].get('award_id') == 'danmu-gold':
                    giftList += '金色弹幕 '
                elif pool[i].get('award_id') == 'uname-gold':
                    giftList += '金色昵称 '
                elif pool[i].get('award_id') == 'title-92':
                    giftList += '年兽头衔 '
                elif pool[i].get('award_id') == 'title-89':
                    giftList += '爆竹头衔 '
                elif pool[i].get('award_id') == 'title-140':
                    giftList += '秋田君 '
                elif pool[i].get('award_id') == 'gift-3':
                    giftList += 'B坷拉 '
                elif pool[i].get('award_id') == 'gift-4':
                    giftList += '喵娘 '
                elif pool[i].get('award_id') == 'gift-109':
                    giftList += '红灯笼 '
                elif pool[i].get('award_id') == 'guard-3':
                    giftList += '舰长 '
                    tmp1 += '舰长 '
                elif pool[i].get('award_id') == 'award-calendar':
                    giftList += '台历 '
                    tmp1 += '台历 '

            #sendEmail('本时段礼物','第 ' + str(counter) + ' 池' + '\n\n' + giftList,'582981961@qq.com')

            if tmp1 != ' ':
                sendEmail('特殊礼物出现了','第 ' + str(counter) + ' 池' + '\n\n' + '本时段礼物:' + tmp1,'582981961@qq.com')
                sendEmail('特殊礼物出现了','第 ' + str(counter) + ' 池' + '\n\n' + '本时段礼物:' + tmp1,'378792351@qq.com')

            ROUND = counter
            
    time.sleep(0.5)
