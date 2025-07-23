"""
子类写了父类中的方法，父类中的方法会失效

重写的方法：
    父类名.父类方法名(self，参数）
"""
class IphoneV1:
    attr = "mobile phone"
    __attr2 = "1000"

    def __init__(self, name):
        self.name = name

    def call(self):
        pass

# class IphoneV2(IphoneV1):
#     # 对此方法的拓展
#     def __init__(self, name, price):
#         # 父类方法重写,方法1
#         IphoneV1.__init__(self, name)
#         # 方法2
#         # super().__init__(name)
#         # 定义新功能
#         self.price = price
#         # 父类方法的执行代码更新
#         print(f"电话的价格{self.price},{self.name}的功能打电话")
#
#     def send_msg(self):
#         print("发短信")
#
#     def music(self):
#         print("放音乐")

iphone = IphoneV1()
iphone.call()

