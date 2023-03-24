# import math
#
# count = 0
# for n in range(2, 300):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             break
#     else:
#         print("{:<5}".format(n), end=" ")
#         count += 1
# print("\n", count)


# n = int(input("输入数列的项数:>"))
# x1 = 1
# x2 = 1
# count = 2
# print("{:<4}{:<4}".format(x1, x2), end="")
# for i in range(3, n + 1):
#     x3 = x1 + x2
#     count += 1
#     print("{:<4}".format(x3), end="")
#     if count % 4 == 0:
#         print()
#     x1, x2 = x2, x3


# s = "http://sports.sina.com.cn/"
# count = s.count(s)
# print(count)
#
# index_com = s.find("com")
# print(index_com)
#
# s_ = s.replace(".", "-")
# print(s_)
#
# print(s[7:13:1])
# print(s[-12:-8:1])
#
# s_max = s.upper()
# print(s_max)
#
# s_len = len(s)
# print(s_len)
#
# s_cat = s + "index"
# print(s_cat)


# count = 0
# for year in range(2000, 3000 + 1):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(year, end=" ")
#         count += 1
#         if count % 10 == 0:
#             print()


# n = int(input("请输入一个比17大的数:>"))
# if n < 17:
#     print("输入错误!")
# else:
#     multiple = n // 17
#     print(f"{n}以内最大能被17整除的数为:>{multiple * 17}")


# import random
# import math
# a = random.randint(1, 100)
# b = random.randint(1, 100)
# c = random.randint(1, 100)
# print(a, b, c)
# print(a, b, c)
# gcd_abc = math.gcd(a, b, c)
# print(a, b, c, "最大公约数为:>", gcd_abc)
# multiple_a = a // gcd_abc
# multiple_b = b // gcd_abc
# multiple_c = c // gcd_abc
# mcm_abc = multiple_a * multiple_b * multiple_c * gcd_abc
# print(a, b, c, "最大公倍数为:>", mcm_abc)

