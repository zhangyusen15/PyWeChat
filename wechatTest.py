# coding=utf-8

import itchat


#friends = itchat.get_friends(update=True)


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print msg.Text
    if msg.User["NickName"]==u"趣":         # response to certain user
        if "250" in msg.Text:               # if we get certain info
            return u"我也想你啦[Kiss]"
        elif "251" in msg.Text:
            return u"1"
        elif u"呵" in msg.Text:
            return u"不许呵！[Kiss]"
        elif u"[Trick]" in msg.Text:
            return u"[Trick][Trick][Trick]"
        elif u"[Smirk]" in msg.Text:
            return u"[Smirk][Smirk][Smirk]"
        elif u"午安" in msg.Text:
            return u"午安[Kiss]"
        elif u"哼" in msg.Text:
            return u"唉..."

if __name__=='__main__':
    #itchat.auto_login(hotReload=True)

    #itchat.run()

    import random
    print random.randint(0,1)
