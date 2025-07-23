import random

# 生成随机整数,包含边界值
res = random.randint(0,3)
print(res)

# 生成随机小数(0-1之间),不包含边界值
res2 = random.random()
print(res2)

# 生成指定范围的小数
res3 = random.uniform(1,20)
print(res3)

# 从列表中随机选取一个数据
li = [1,2,3,4,5,6,7,8,9]
res4 = random.choice(li)
print(res4)