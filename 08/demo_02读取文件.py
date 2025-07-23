"""
操作文件的步骤：
    打开：open
    操作：
        read:默认读取所有内容
        readline：读取一行
        readlines:读取一整行,返回一个列表

    关闭:close


"""
f = open(file='result.txt',mode="r",encoding="utf-8")
res = f.readline()

print(res)

f.close()