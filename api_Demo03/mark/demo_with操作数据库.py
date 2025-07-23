"""
with:
    启动对象上下文管理器的关键字

    上下文管理器协议:
            __enter__:
            __exit__:
            如果一个类中定义了如上两个方法,那么该类就实现了上下文管理器协议（可以通过with操作）


"""
import pymysql
# 创建连接
con = pymysql.connect(host="api.lemonban.com",
                      port=3306,
                      user="future",
                      password="123456",
                      charset="utf8")
                      #
                      #cursorClass = pymysql.cursors.DictCursor)


# 创建游标对象,with会自动提交事物
with con as cur:
    sql = "SELECT leave_amount FROM futureloan.member WHERE mobile_phone='13499009876';"
    #res = con.cursor().execute(sql)
    res1 = con.cursor().fetchall(sql)


print(res1)


