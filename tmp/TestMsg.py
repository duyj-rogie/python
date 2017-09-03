#!/usr/bin/python
# -*- coding: UTF-8 -*-

from wxpy import *


bot = Bot(cache_path = True)
# friends = bot.friends(update=True)
male = female = other = 0

# for i in friends[1:]:
#     sex = i.sex
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other += 1
# total = len(friends[1:])
# print(male);
# print(female);
# print(other);

# # 提取好友签名，并去掉span，class，emoji，emoji1f3c3等的字段
# signatures = []
# for i in friends:
#     signature = i.signature.strip().replace("span", "").replace("class", "").replace("emoji", "")
# # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
#     rep = re.compile("1f\d.+")
#     signature = rep.sub("", signature)
#     signatures.append(signature)
# # 拼接字符串
# text = "\n".join(signatures)
# print(text)

my_friend = bot.friends(update=True).search('Korn', sex=MALE)[0]

# my_friend.send('@img@wx_001.jpg')
#
# my_friend.send_image('wx_001.jpg')

#  注册获得个人的图灵机器人key 填入
dear = bot.friends(update=True).search("Korn"[0])

tuling = Tuling(api_key='480542c907514afd8538b4d42fc20bad')

groups = ensure_one(bot.groups().search('groupTest'))

# 使用图灵机器人自动与指定好友聊天


@bot.register(my_friend)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg, at_member=False)

embed()


# for member in groups.members:
#     print (member)

# groups.remove_members(my_friend)
# groups.add_members(my_friend)

# print (groups.owner)
