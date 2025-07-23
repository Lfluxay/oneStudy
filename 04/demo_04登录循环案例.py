"""
输入密码账号登录，错则重输入，对则退出
"""
username = "jack"
password = "123456"
sta = 0
while sta == 0:
    user = input("请输入账号：")
    psd = input("请输入密码：")
    if user == username and psd == password:
        print("login")
        sta = 1
    else:
        print("again")

while True:
    user = input("请输入账号：")
    psd = input("请输入密码：")
    if user == username and psd == password:
        print("login")
        break
    else:
        print("again")