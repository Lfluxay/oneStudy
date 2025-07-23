"""
模块：
    一个.py结尾的文件就可以是一个模块

包：
    一个包含__init__.py的文件夹，就可以称之为一个包

注意点：导入不出错，命名要规范，尽量简短


模块和包的导入：
    导入的关键字
        from
        import

    模块的导入：
        import 模块名

        自定义模块导入，根目录开始层级向下找
        from 文件位置 import 模块名

    包的导入


"""

# 模块导入
# import fluxay
# from test import fluxay
# fluxay.func(5)


# 包的导入
# from unittest import removeResult
# import requests
# from requests import session


# 不推荐
from demo import demo
print(demo)


# 推荐
from demo import test_01

from demo import test_02

print(test_01.name)

print(test_02.name)
