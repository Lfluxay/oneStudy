"""
with xxx as xxx：

    上下文管理器协议的启动器

with open操作文件会自动关闭文件

"""
# 打开文件，返回文件的句柄
with open(file="result.txt", mode="r", encoding="utf-8")as f:
    print(f.read())

