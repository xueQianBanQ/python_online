"""
#以为Input的返回值为str
a = int(input('请输入一个数'))
#a = int(a)
b = int(input('请输入另一个数'))
#b = int(b)
print(a + b)
"""
"""  
print(5 / 2) #2.5
print(5 // 2)#2  整除
print(5 % 2)#1   取模
print(2 ** 4)
"""
"""
print(-9 // 4)
print(9 // -4)
print(-9 % 4)
print(9 % -4)
"""
''''
#链式开辟的空间 a, b, c的地址都是一样的
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))
'''
"""
print("---------解包赋值---------")
a, b, c = 20, 30, 40
print(a, b, c)
print(a,b,c)

a, b = 20, 30
print("交换前")
print('a=', a)
print('b=', b)
print('交换后')
a, b = b, a
print("a=", a)
print("b=", b)
"""
"""
#比较运算符的结果为布尔值
a, b = 20, 30
print(a > b)
# == 比较的是value
# is 和 is not  比较的是id (地址)
a, b = 10, 10
print(a == b)
print(a is b)

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(id(list1))
print(id(list2))
print(list1 is list2)
"""
"""
'''and  or  not'''
'''in 和 not in'''
s = "hello world"
print('w' in s)
print('a' not in s)
print(' ' in s)
print(''in s)
"""
"""
>> 和 << 的运算规则和C语言的规则是一样的
"""
"""
a = 50
if a > 100:
    print("hehe")
elif a > 50:
    print("haha")
else:
    print("bit")
"""
#score = int(input("请输入您的成绩"))
""""" 之前的语言方式
if score >= 90 and score <= 100:
    print("A级")
elif score >= 80 and score < 90:
    print("B级")
elif score >= 70 and score < 80:
    print("C级")
elif score >= 60 and score < 70:
    print("D级")
elif score >= 0 and score < 60:
    print("E级")
else:
    print("输入错误")
    """
"""
#python独有的表达方式
if 90 <= score <= 100:
    print("A级")
elif 80<= score < 90:
    print("B级")
elif 70<= score < 80:
    print("C级")
elif 60 <= score < 70:
    print("D级")
elif 0 <= score <60:
    print("E级")
else:
    print("输入错误")
"""

"""
######################python 是严格按照缩进来进行的
money = 70
if money > 60:
    print("hehe")
    if money >70:
        print("haha")
else:
    print("bit")

money = 70
if money > 60:
    print("hehe")
    if money > 70:
        print("haha")
    else:
        print("bit")
        """

"""
mun_a = int(input("请输入一个数:>"))
mun_b = int(input("请输入另一个数:>"))
"""
"""
if mun_a > mun_b:
    print(mun_a, "大于", mun_b)
else:
    print(mun_b, "大于", mun_a)

#print((mun_a, "大于", mun_b) if mun_a > mun_b else (mun_b, "大于", mun_a))
print(str(mun_a)+ "大于" + str(mun_b) if mun_a > mun_b else str(mun_b) + "大于" + str(mun_a))
   """
"""
if(20 > 10):
    pass
else:
    pass
"""
"""
r = range(10)
print(list(r))
r = range(1, 10)
print(list(r))
r = range(0, 10, 2)
print((list(r)))
"""
"""
a = 0
while a < 10:
    print(a)
    a+=1
    """
"""
a = 10
for item in "python":
    pass
print(a)
print(item)
"""


