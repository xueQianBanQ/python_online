# str = "love af"
# print(str.split('1'))


# a, b, c = map(int, input("请输入三个整数(用逗号隔开)").split(","))
# print("a、b、c 中原来的值分别为:", a, b, c)
# a, b, c = c, a, b
# print("交换后a、b、c中的值分别为:", a, b ,c)


# maths, chinese, english = map(int, input("请输入3门课程的成绩:").split(","))
# sum = maths + chinese + english
# print("总分是:", "%.2f"%(sum))


# import math
# radius = eval(input("请输入圆的半径:"))
# Perimeter = 2 * radius * math.pi
# Area = radius ** 2 * math.pi
# print("圆的半径:", radius, "周长是:", "%.3f"%(Perimeter), "面积是:", "%.3f"%(Area))


import random
price = random.randint(10, 50)
payment = random.randrange(200, 501, 1)
gap = payment - price
temp = gap
money_100 = gap // 100
gap %= 100
money_50 = gap // 50
gap %= 50
money_10 = gap // 10
gap %= 10
money_5 = gap // 5
money_1 = gap % 5
print("应付款:", price)
print("实付款:", payment)
print("找零:", temp)
print("100元:", f"{money_100}张")
print("50元:", f"{money_50}张")
print("10元:", f"{money_10}张")
print("5元:", f"{money_5}张")
print("1元:", f"{money_1}张")

