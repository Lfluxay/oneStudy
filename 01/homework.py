# 01
a = "hello"
b = "python18"
c = "!"
print(" ".join((a,b,c)))

# 02
s = "abcdefghijk"
# defg
print(s[3:7])
# cgk
print(s[2:11:4])


# 03
str1 = "PHP is the best, programing, $language in, the world! "
print(str1.find("$"))
print(str1.replace("PHP","python"))
print(str1.split(","))

# 04
price = int(input("请输入橘子的价格："))
jin = int(input("请输入橘子的重量："))
money = jin*price
print("橘子价格为{}元每斤，购买{}斤，应支付价格为{}元".format(price,jin,money))


