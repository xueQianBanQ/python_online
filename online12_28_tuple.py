########################元组
"""元组的创建"""
""""
t = ("world", "hello", 98)#元组为不可变序列（没有增、删、改）
print(t)
print(type(t))
t2 = tuple(("world", "hello", 98))
print(t2)
t3 = "world", "hello", 98
print(t3)
print(type(t3))
"""
#如果元组中只有一个元素，不能省略后面的逗号
"""
t = ("python")
print(t, type(t))
t = ("python", )
print(t, type(t))
"""
"""
t = (10, [20, 30], 9)
t[1][0] = 10
#t[1] = 10# 这是不可以的， 只能改变地址中元素的量， 不可以改变地址
print(t)#因为元组是不可变序列
"""
######################集合
"""
s = set(range(11))
print(s, type(s))
s = {1, 2, 3, 3, 7, 9, 7}#不能有重复的元素，否则会被代替
print(s)
s2 = set((1, 2, 4, 4, 5,98))#因为元组的序列是无序的，所以强制类型转换掉后，不一定是一开始的顺序
print(s2)
s3 = set('python')
print(s3)
"""
"""
s = set((1, 2, 3))
print(s)
s.add(5)
print(s)
s.update((4, 5, 6))
print(s)
s.remove(4)
#s.remove(9)#KeyError: 9
print(s)
s.discard(9)#不存在， 不会抛出异常
print(s)
s.pop()#删除第一个元素， 且不能传参,不然会报错---------列表是删除最后一个
print(s)
s.clear()#清空      
print(s)
"""
