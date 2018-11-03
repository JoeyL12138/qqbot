# -*- coding: utf-8 -*-
import json
import requests
import random
import time

 
KEY = 'c6527bc6f1214306a19f1c126f476672'    # change to your API KEY
url = 'http://www.tuling123.com/openapi/api'

def onQQMessage(bot, contact, member, content):
    if '-stop' in content:
        if '-stop' == content:
            bot.SendTo(contact,'Please enter the password\nformat: -stop *****',resendOn1202=False)
        else:
            tempList = content.split()
            if tempList[0] == '-stop':
                if tempList[1] == '12345':
                    bot.SendTo(contact,'Password is correct!',resendOn1202=False)
                    bot.SendTo(contact,'The robot is shutdown!',resendOn1202=False)
                    bot.Stop()
                else:
                    bot.SendTo(contact,'Password is wrong!!!\nPlease try again',resendOn1202=False)
        return

    elif bot.isMe(contact, member):
        return


    if contact.uin == '566314155' or contact.uin == '3332785914':
        req_info = content.encode('utf-8')
        query = {'key': KEY, 'info': req_info}
        headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

        r = requests.get(url, params=query, headers=headers)
        res = r.text
        message = json.loads(res).get('text').replace('<br>', '\n')
        

        # randomly wait 5-240 seconds
        waitTime = random.randint(5,240)
        #bot.SendTo(contact,str(waitTime),resendOn1202=False)

        time.sleep(waitTime)

        bot.SendTo(contact,message,resendOn1202=False)


