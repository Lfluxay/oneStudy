"""
open:
    内置函数
    参数1：file---传文件名或者路径
    参数2：mode---文件打开的模式
        r：只读
        w：
    参数3：encoding----指定的编码格式

操作文件的步骤：
    打开：open
    操作：r
    关闭:close


"""
f = open(file='result.txt',mode="r",encoding="utf-8")
res = f.read()

print(res)

f.close()