import itchat

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)
print friends