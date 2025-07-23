from decimal import Decimal
from unittest import TestCase
a = 10
b = 10.10

res = Decimal("10.10")
print(res, type(res))

test = TestCase()
# 断言失败
# test.assertEqual(b, res)
# AssertionError: 10.1 != Decimal('10.10')

# 成功断言
test.assertEqual(b, float(res))

# python中的浮点数精度存在问题

print(3.33 - 2.11)
print((3.31*100 - 2.11*100)/100)

# 注意点：创建decimal类型，需要传入字符串类型，否则会出现精度丢失
# decimal是Python中用来表示浮点数精度的一种数值类型

