#!/usr/bin/python
# -*- coding: UTF-8 -*-

from wxpy import *

bot = Bot(cache_path=True)

# 自动添加好友的条件
addfriend_request = '加好友'


# 注册好友请求类消息
# 自动接受验证信息中包含 'wxpy' 的好友请求

myfrends = bot.friends()


@bot.register(myfrends, enabled=True)
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    print(msg)
    # if addfriend_request in msg.text.lower():
    # 接受好友 (msg.card 为该请求的用户对象)
    new_friend = bot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('I am robot, welcome!')


embed()
