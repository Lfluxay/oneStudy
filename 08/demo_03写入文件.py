"""
操作文件的步骤：
    打开：open
    操作：
        w:覆盖写入
            文件不存在，则会创建新的一个文件
        a:追加写入，不覆盖原有内容
            文件不存在，则会创建新的一个文件
    关闭:close

"""
# a模式
# f = open(file='result01.txt',mode="a",encoding="utf-8")
#
# res = f.write("套你猴子,1111\n")
#
# print(res)
#
# f.close()


# w模式
# f = open(file='./test/result01.txt', mode="r", encoding="utf-8")
#
# res = f.read()
#
# print(res)
#
# f.close()


# repr-----拓展
print("hello")
print(repr("hello"))
