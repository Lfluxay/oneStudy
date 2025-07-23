"""
元组：
    1.可以存放任意类型的数据
    2.有序的
        支持索引
        支持切片
    3.元组中的元素是不变的
        定义后，不可进行增/删/改
    4.查找
        通过索引取值
        index:查找指定元素索引
        count：统计某个元素出现的次数
"""
t = ('jack', 18, 'man')
print(t[1])
print(t[1:])
print(t.index('man'))
print(t.count('jack'))





