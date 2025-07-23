"""
        默认参数self的意思：表示对象本身
        使用对象调用方法，那个对象调用方法，self表示的就是那个对象
"""

class Cat:
    leg = 4
    tail = 1
    eye = 2

    def catch(self, addr, num):
        # print(self.name)
        print("{} catch mouse in {}, catch {}".format(self.name, addr, num))
        return "catch 3 mouse"

# 通过类属性创建对象
coffee = Cat()
single = Cat()

# 通过类实例化对象
coffee.name = "jack"
single.name = "rose"

# 通过对象调用方法
res = coffee.catch("tree", 1)
print(res)
single.catch("house",100)

