"""
数值：
    算术运算 + - * /
    比较运算 > < >= <= != ==

其他运算符：
    1、逻辑运算
        and：全真为真
        T T    T
        T F    F
        F T    F
        F F    F
        or：一真为真
        T T    T
        T F    T
        F T    T
        F F    F
        not：取反
        NOT F   T
        NOT T   F

    2、成员运算
        in:成员判断
        not in:非成员判断
        (字典成员运算，默认判断键，如果判断值则.values，需要进行类型转换)

    3.身份运算符（判断数据id是否一致）
        is:
        is not:

    == 和 is的区别？

    4.赋值运算符
        =
        +=
        -=
        *=
        %=
        /=
"""
l1 = [1,2,3,4]
l2 = l1
l3 = l1.copy()
print(l1,id(l1))
print(l2,id(l2))
print(l3,id(l3))
if l1 is l2:
    print("T")
else:
    print("F")
