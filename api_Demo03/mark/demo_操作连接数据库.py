"""
操作数据库：
    pymysql模块：

"""
import pymysql
# 创建连接
con = pymysql.connect(host="api.lemonban.com",
                      port=3306,
                      user="future",
                      password="123456",
                      charset="utf8")
# 创建游标对象
cur = con.cursor()

# 执行sql语句
sql = ""
res = cur.execute(sql)
print(res)


# 提交事物,如果涉及到增删改的操作，需要提交事物才能生效
con.commit()

# 关闭游标
cur.close()

# 断开连接
con.close()
