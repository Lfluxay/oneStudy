from configparser import ConfigParser

# 实例化
cp = ConfigParser()

# 调用方法读取配置文件
cp.read("config.ini", encoding="utf-8")
# 设置写入内容
cp.set('mysql', 'name', 'admin')
# 写入操作
with open('config.ini', 'w', encoding='utf-8') as f:
    cp.write(fp=f)