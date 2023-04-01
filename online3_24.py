# sort 和 sorted函数
a = (2, 3, 1)
b = [2, 3, 1]
b.sort(reverse=True)
print(b)
b.sort()  # 默认是reverse = False即升序
print(b)
b = sorted(b, reverse=True)
print(b)
# a = sort()#元组tuple不可以使用sort函数，因为tuple是常量和字符串一样是不可变序列
# 但是由于sorted改变的不是原序列，所以可以使用sorted函数
c = sorted(a)
print(a)
print(c)  # 但返回的是列表

c = (7, 9, 8)
print(a + c)  # 返回的是新开辟的空间，所以可以
# print(a + b)  # 不可以进行夸类型运算，Python在这点还是挺严的，就比如‘A’ + 1 就是不可以，想要的话还要通过ord 和 chr 来实现。


# c = a.copy()  # 不可以
c = b.copy()  # 深拷贝
c.append(5)
print(c)
print(b)
d = b  # 浅拷贝
d.append(5)
print(d)
print(b)


c = a.count(1)
print(c)

# del a[:]
del a

