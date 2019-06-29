#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import itchat
import random
import time

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print msg.Text
    r = {}

    autoResponse = open("autoresponse.txt",'r')
    autoResponse.seek(0)
    for x in autoResponse:
        get = x.split(",")[0].strip()
        response = x.strip().split(",")[1:]
        r[get] = response
    autoResponse.close()

    autoResponse2 = open("autoresponse2.txt",'r')
    autoResponse2.seek(0)
    r2 = []
    for x2 in autoResponse2:
        r2.append(x2.strip())
    autoResponse2.close()

    k = r.keys()
    if msg.User["NickName"]==u"趣":
        for kk in k:
            if u"%s"%kk in msg.Text:
                return u"%s"%r[kk][random.randint(0,len(r[kk])-1)]
    else:
        if int(r2[0])>0:
            time.sleep(int(r2[0]))
            return u"%s"%r2[random.randint(1,len(r2))]

if __name__=='__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
