import pymysql
from common.handle_conf import conf

class HandleDB:

    def __init__(self):
        self.con = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            charset="utf8")

    def find_one(self, sql):
        """查询一条数据"""
        with self.con as cur:
            cur.cursor().execute(sql)

        return cur.cursor().fetchone()

if __name__ == "__main__":
    sql = "Select * FROM futureloan.member LIMIT 5;"
    db = HandleDB()
    res = db.find_one(sql)
    print(res)