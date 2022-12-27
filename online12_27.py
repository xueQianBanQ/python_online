
"""100到999之间的水仙花数"""
"""
for i in range(100, 1000):
    unit = i % 10
    decade = i % 100 // 10
    hundred = i // 100
    if i == unit**3 + decade ** 3 + hundred ** 3 :
        print(i)
        """
###############循环和else之间的使用
""""
for i in range(3):
    password = input("请输入密码")
    if password == "8888" :
        print("输入正确")
        break
    else:
        print("密码输入错误")
else:
    print("三次均输入错误")
"""

#####while循环一样， 正常循环结束，会执行相对应的else的语句


####打印9*9乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j)+"*"+str(i)+"="+str(i * j), end = "\t")
    print()
"""

##########################################列表
"""
lst = ["hello", "world", 98]
print(lst[0])
print(id(lst))
print(id(lst[0]))
print(id(lst[1]))
print(id(lst[2]))
#第二种创建列表方法
lst2 = list(["hello", "world", 98])
print(type(lst2))
"""

"""
# list.index()
lst = list(["hello", "world", 98, "hello"])
print(lst.index('hello'))# 返回多个元素中的第一个
print(lst.index("world", 1, 4))
"""
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst[1:8:2])
lst2 = lst[1:8:2]
print("原列表", id(lst))
print("切割后", id(lst2))

print(lst[::-1])
print(lst[9:0:-1])
print(lst[7:0:1])#返回空列表
"""
###############################增加列表元素
"""
lst = [1, 2, 3]
lst.append("你好")
print(lst)
lst2 = ["hello", "你好"]
print(lst2)
#lst.append(lst2)#加的是一个列表
lst.extend(lst2)#加的是的两个元素
print(lst)
lst.insert(1, 20)
print(lst)
lst[1:1] = [90, "world"]
print(lst)
lst[1:] = ["hello", "world"]
print(lst)
"""
################################删除列表元素
""""
arr1 = [1, 2, 3, 4, 5, 3]
arr1.remove(3)
print(arr1)
arr1.pop(2)
print(arr1)
arr1.pop()#删除列表的最后一个元素
print(arr1)
new_arr1 = arr1[1:3]#保留哪些（切片）   且产生新数组
arr1[1:3] = []#切片删除   不想要的给予空列表
print(new_arr1)
print(arr1)
arr1.clear()#清空列表
print(arr1)
del arr1
#print(arr1)#直接报错，因为已经删除了这个变量， 相当于free()了这个列表的动态内存，并给予了NULL
"""
"""
lst = [1 ,3, 2, 4, 3, 0, 9]
lst.sort()#是在原列表上修改
print(lst, id(lst))
lst.sort(reverse = True)
print(lst, id(lst))

new_lst = sorted(lst)
print(new_lst)
new_lst = sorted(lst, reverse = True)
print(new_lst)
"""
########################如何用循环创建列表
lst = [i for i in range(1 ,11)]
print(lst)
for i in range(1, 11):
    lst[i - 1] = i
print(lst)