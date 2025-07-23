"""
一家前场在降价促销,需要编写一个程序,输入购买前品的总价格,再打印出折扣和最终价格
    要求如下：
        會如果购买总金额0-49几(包含元相49元)之间,不打折
        如果购买总金额50-100元(包含50元和100元)之间,会给打九折
        如果购买总合额人于100元,会给打八折
"""
# price = int(input("请输入你此次购物金额："))
# if 0 <= price <= 49:
#     print("你本次购物的价格{},不打折".format(price*1))
# elif 50 <= price <= 100:
#     print("你本次购物的价格{}，享受9折优惠".format(price * 0.9))
# elif price > 100:
#     print("你本次购物的价格{}，享受8折优惠".format(price * 0.8))
# else:
#     print("你的输入有误！")

"""
提示用广输入一个整数,判斯这个数是否为3和5的公倍数(同时被3和5整除)
能整除则打印:您输入的是3和5的公倍数,获得双十—100元抵用券
不能整除则打印:你与优惠券错过啦
"""

# num = int(input("请输入一个整数："))
# if num%3 == 0 and num%5 == 0:
#     print("您输入的是3和5的公倍数,获得双十—100元抵用券")
# else:
#     print("你与优惠券错过啦")


"""
编写一个程序,使用循环打印0-100(包括0和100)之间的偶数
"""
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         print("偶数{}".format(i))
#     i += 1

"""
实现文字版的剪刀石头布游戏(扩展题)
1、运行程序提示用户输入要出的拳:石头(1)/剪刀(2)/布(3)/退出(4)
2、电脑随机出拳
3、比较胜负,显示：用户胜、负还是平局。
运行如下图所示(提小: while循环加条件判断,做判断时建议先分析胜负的情况)
user    random      
 1         2
 2         3
 3         1
"""
# import random
# print("------------开始-------------")
# print("请按照提示输入")
# li = ["石头", "剪刀", "布"]
# while True:
#     print("石头(1)/剪刀(2)/布(3)/退出(4)")
#     user = int(input("请输入选项:"))
#     computer = random.randint(1, 3)
#     if 1 <= user <= 3:
#         if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3  and computer == 1):
#             print("你赢了，玩家胜利,玩家出-{},电脑出-{}".format(li[user-1],li[computer-1]))
#         elif user == computer:
#             print("平局啦，玩家出-{},电脑出-{}".format(li[user-1],li[computer-1]))
#         else:
#             print("你输了，电脑胜利，玩家出-{},电脑出-{}".format(li[user-1],li[computer-1]))
#     elif user == 4:
#         print("exit")
#         break
#     else:
#         print("error，again")

import random
print("------------开始-------------")
print("请按照提示输入")
li = ["石头", "剪刀", "布"]
while True:
    print("石头(1)/剪刀(2)/布(3)/退出(4)")
    user = int(input("请输入你的出拳："))
    npc = random.randint(1,3)
    if 1 <= user <=3:
        if (npc - user == 1) or (user - npc == 2):
            print("玩家获胜，玩家的出{}，npc的出{}".format(li[user-1], li[npc-1]))
        elif user == npc:
            print("平局，玩家的出{}，npc的出{}".format(li[user-1], li[npc-1]))
        else:
            print("电脑获胜，玩家的出{}，npc的出{}".format(li[user-1], li[npc-1]))
    elif user == 4:
        print("exit!")
        break
    else:
        print("输入有误，重新输入！")