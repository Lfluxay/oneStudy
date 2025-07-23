"""
简述异常处理流程，以及每个流程怎么处理的？
"""


"""
用户输入一个数值n，打印1到n（包含n）之间的所有偶数，及其偶数个数，及其他们的平均值
如果用户输入的非数值，提示重新输入
"""
def func():
    while True:
        try:
            num = int(input("请输入一个数字:"))
        except Exception as e:
            print("input error",e)
            continue
        else:
            if num <= 1:
                print("num must > 1")
                continue
            else:
                result = []
                for i in range(1, num+1):
                    if i % 2 == 0:
                        result.append(i)
                print("偶数的结果 {}".format(result))
                print("偶数的个数 {}".format(len(result)))
                avg = sum(result) / len(result)
                print("计算的平均值 {}".format(avg))
                break

func()

"""
猜拳游戏升级版
输入错误提示异常
"""
import random
def func():
    print("--------开始--------")
    print("请按照如下提示出拳：")
    li = ["剪刀", "石头", "布"]

    while True:
        print("1.剪刀", "2.石头", "3.布", "4.exit")
        try:
            user = int(input("请输入你的选项："))
        except:
            print("input error，try again!")
            continue
        computer = random.randint(1, 3)
        if 1 <= user <= 3:
            if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
                print("你赢了，玩家胜利,玩家出-{},电脑出-{}".format(li[user - 1], li[computer - 1]))
            elif user == computer:
                print("平局啦，玩家出-{},电脑出-{}".format(li[user - 1], li[computer - 1]))
            else:
                print("你输了，电脑胜利，玩家出-{},电脑出-{}".format(li[user - 1], li[computer - 1]))
        elif user == 4:
            print("exit")
            break
        else:
            print("input error，try again!")

func()
