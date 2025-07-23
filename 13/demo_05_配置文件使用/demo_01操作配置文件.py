# 导包
from configparser import ConfigParser

# 1.创建一个配置文件解析器对象
cp = ConfigParser()

# 2.读取配置文件中的内容到配置文件解析器中
cp.read('config.ini')

# 3.读取配置内容
# 方法1：使用get方法读取的配置文件都会被当成字符串
res = cp.get('logging', 'file')
print(res, type(res))

# 方法2：getint，读取整型
res2 = cp.getint('mysql', 'port')
print(res2, type(res2))

# 方法3：getboolean，读取布尔值
res3 = cp.getboolean("test_data", 'bool')
print(res3, type(res3))

# 方法4：getfloat，读取浮点型
