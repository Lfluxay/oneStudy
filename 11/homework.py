"""
1、通过继承定义如下三个类: PhoneV1 PhoneV2 PhoneV3
PhoneV1
    类属性:attr=“移动电话"
    实例属性:name(品牌型号)price价格),(year)生产年份
    方法:打电话
PhoneV2
    类属性:attr="移动电话"
    实例属性:name(品牌型号)price价格),(year)生产年份,摄像头像素(pixel)
    方法:打电话,听音乐,发短信,拍照
PhoneV3
    类属性:attr="移动电话"
    实例属性:name(品牌型号)price价格),(year)生产年份,摄像头像素(pixel),屏幕大小(screen)
    方法:打电话,听音乐,发短信,拍照,看视频
"""
class PhoneV1:
    attr = "移动电话"

    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def call(self):
        print(f"{self.name}有打电话的功能")


class PhoneV2(PhoneV1):
    def __init__(self, name, price, year, pixel):
        PhoneV1.__init__(self,name, price, year)
        self.pixel = pixel

    def music(self):
        print(f"{self.name}有听音乐的功能")

    def send_msg(self):
        print(f"{self.name}有发短信的功能")

    def photo(self):
        print(f"{self.name}有拍照的功能")


class PhoneV3(PhoneV2):
    def __init__(self, name, price, year, pixel, screen):
        PhoneV2.__init__(self, name, price, year, pixel)
        self.screen = screen

    def video(self):
        print(f"{self.name}有看视频的功能")

res = PhoneV3("iphone12",8999,2021,"1200W","2k")
print(res.call())

"""
有一组数据：
{'case_id':1, 'method':'post', 'url':'/login/api',
'data':'123','actual':'fail'，'excepted':'pass'}
分别设置键值为属性名属性值
"""

# data = {'case_id':1, 'method':'post', 'url':'/login/api','data':'123','actual':'fail','excepted':'pass'}
# class CaseData:
#     pass
#
# for k, v in data.items():
#     setattr(CaseData,k,v)
# print(CaseData.__dict__)