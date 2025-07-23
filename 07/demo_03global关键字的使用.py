"""
在函数内部定义或修改全局变量

global：
    声明函数内部操作的全局变量

"""
number = 100

def func():
    #print(number+100)
    global number,name
    name = "jack"
    number = number +100

func()
print(number)
print(name)


def func2():
    print("func2:",name)

func2()