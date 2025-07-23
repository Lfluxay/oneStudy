"""
操作文件的步骤：
    打开：open
    操作：
        图片视频文件写入或读取
        rb：二进制模式打开,只读
        wb：二进制模式打开,覆盖写入
        ab：二进制模式打开,追加写入
            ---------拓展
                    r+:
                    a+:
                    w+:
                    rb+：
                    wb+：
                    ab+：



    关闭:close

"""
f = open(file="支付截图.jpeg",mode="rb",)
res = f.read()
print(res)


f2 = open(file="支付截图01.jpeg",mode="wb")
res2 = f2.write(res)
print(res2)

f.close()
f2.close()

