"""
raise:
    主动抛出异常

"""
# raise NameError('xxx error')


# 应用场景,限定参数类型，非指定类型，直接主动抛出异常
def add(a,b):
    if not isinstance(a,(int,float)):
        raise ValueError("a int ")
    if not isinstance(b,(int,float)):
        raise ValueError("b int")
    return a+b

res = add("abs",222)
print(res)