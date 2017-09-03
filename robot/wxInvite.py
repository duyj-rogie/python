#!/usr/bin/python
# -*- coding: UTF-8 -*-

from wxpy import *

bot = Bot(cache_path=True)


admin_puids = frozenset(['XX', 'YY'])   #不可变集合
# admins = list(map(lambda x: bot.friends().search(puid=x), admin_puids))


@bot.register(Friend, msg_types=TEXT)
def invite(msg):
    print (msg.sender)
    msg.sender.send("success")
    # if user in group:
    #     content = "您已经加入了{} [微笑]".format(group.nick_name)  # 经过format格式化的内容传递到{}
    #     user.send(content)
    # else:
    #     group.add_members(user, use_invitation=True)


embed()
