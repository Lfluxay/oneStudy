"""
class Cat:
    leg = 4

类属性怎么定义？
    直接定义在类里面的变量
实例属性怎么定义？
    先实例化对象
        jack = Cat()
        对象 = 类名()
    然后实例属性
        jack.name = "tom"
        对象.属性名 = 属性值
    __init__方法中：
        self.属性名 = 属性值

"""

"""
实例方法中的self代表什么？
    self表示对象本身，什么对象调用这个方法就代表哪个对象

"""

'''
类中的__init__方法在什么时候会调用？
    创建对象的时候会自动调用
'''

"""
封装一个学生类,(自行分辨定义为类属性,还是实例属性)
属性: 身份(学生),     
     姓名,年龄,性别,英语成绩,数学成绩,语文成绩
方法一:计算总分,
方法二:计算三科平均分,
方法三:打印学生的个人信息。
"""

class Student:
    id = "学生"

    def __init__(self, name, age, gender, english, math , chinese):
        self.name = name
        self.age = age
        self.gender = gender
        self.english = english
        self.math = math
        self.chinese = chinese

    def sum_socre(self):
        res = self.english + self.math + self.chinese
        return res

    def avg_score(self):
        res = self.sum_socre() / 3
        return res

    def stu_info(self):
        print("学生名字：{}，年龄：{}，性别:{}".format(self.name,self.age,self.gender))

test_01 = Student("jack",12,"男",90,60,75)
res_sum = test_01.sum_socre()
print("成绩总分：",res_sum)

res_avg = test_01.avg_score()
print("成绩平均分：",res_avg)

test_01.stu_info()



"""
封装一个测试用例类(自行分辨定义为类属性还是实例属性)
属性:用例编号  url地址  请求参数  请求方法  预期结果  实际结果
"""
class TestCase:

    def __init__(self, test_id, test_url, test_prm, test_method, test_result , result):
        self.test_id = test_id
        self.test_url = test_url
        self.test_prm = test_prm
        self.test_method = test_method
        self.test_result = test_result
        self.result = result

test_res = TestCase('用例编号', 'url地址',  '请求参数', '请求方法', '预期结果', '实际结果')

print(test_res.test_id)
"""
封装一个GirL或者Boy类,按照自己找(现有)对象的标准去定义一个类
属性和方法自由发挥
"""