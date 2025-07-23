"""
继承的作用：
    为了提高代码复用效率，子类可以通过继承，得到父类属性和方法，然后再写子类的方法
    私有属性和方法除外(__)

"""

# 继承的模式
class IphoneV1:
    def call(self):
        print("打电话")


class IphoneV2(IphoneV1):
    def send_msg(self):
        print("发短信")
    def music(self):
        print("放音乐")

class IphoneV3(IphoneV2):
    def pay(self):
        print("支付")
    def game(self):
        print("玩游戏")

test = IphoneV3()
test.pay()
test.send_msg()
test.music()
test.call()