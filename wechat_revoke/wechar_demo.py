import itchat
from itchat.content import PICTURE, TEXT, FRIENDS


# 自动回复
@itchat.msg_register([PICTURE, TEXT, ])
def simple_reply(msg):
    if msg['Type'] == TEXT:
        if msg['Content']=='hehe':
            print(msg['FromUserName'])
            # friendList = itchat.get_friends(update=True)[1:]
            # for friend in friendList:
            #     print(friend)
    #     ReplyContent = 'I received message: ' + msg['Content']
    # if msg['Type'] == PICTURE:
    #     ReplyContent = 'I received picture: ' + msg['FileName']
    # itchat.send_msg(ReplyContent, msg['FromUserName'])




# # 自动添加好友
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录，微信不要开启“加好友无需验证”
#     itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


# 遍历好友
# friendList = itchat.get_friends(update=True)[1:]
# for friend in friendList:
#     print(friend)


itchat.auto_login(hotReload=True)
itchat.run()
