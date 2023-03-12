# a = 56
# b = 'a'
# c = a - b
# print(c)
#
# a = int('c')

#python 中不支持字符串转变成ASCII值


#format用法
# a = 1
# b = 2
# print("我是{},他是{}".format(a, b))
# print("{:*^21}".format("请输入:"))#多出来的一个会保存到下面一个

# print("我是",18,"岁")
# print(f"我是 {18} 岁")



# #结构 :<填充字符（字符只能为一种，默认为空白）><对齐方式><宽度>
# # ^:居中， <:左对齐，   >:右对齐
# print("{:*^20}".format("请输入:>")) #如果多出来一个，将放在右边
# print("{:#<20}".format("请输入:>"))
# print("{:8<20}".format("请输入:>"))

# print("{:.2f}".format(3.146124))#含四舍五入
# #将其结合起来
# print("{:*^20.2f}".format(2.13124))


# import math
# def SphereVolume(radius):
#     return 4*math.pi*(radius**3)/3
#
# def CircleRingArea(radius_R,radius_r):
#     return (radius_R**2 - radius_r**2) * math.pi
#
# def ColumnVolume(radius, high):
#     return radius * radius * math.pi * high
#
# def ColumnArea(radius, high):
#     return 2 * radius * math.pi *high + 2 * radius * radius * math.pi
#
#
# SV = SphereVolume(2.11)
# print("{:.2f}".format(SV))
# CR = CircleRingArea(16.2, 9.4)
# print("{:.2f}".format(CR))
# CV = ColumnVolume(66, 24.2)
# print("{:.2f}".format(CV))
# CA = ColumnArea(66, 24.2)
# print("{:.2f}".format(CA))

import math
def CoordinateDistance(x1,y1,x2,y2):
    return math.hypot(x1-x2, y1-y2)


distance = CoordinateDistance(1, 2, 3, 4)
print("{:.2f}".format(distance))