# names = "张三丰,小风"
# guests = list(names)
#
# print(guests)
# guests = names.split(',')
# print(guests)

# dict_a = {'a': 4, 'b': 6};
# print(dict_a['a'])
# dict_a['c'] = 5
# print(dict_a)

# a = "I love you and python."
# a = a.lower()
# counts = {}
# for c in a:
#     counts[c] = counts.get(c, 0) + 1
# print(counts)


# dict_menu = {"汉堡": 15, "鸡翅": 10, "薯条": 6, "骨肉相连": 12, "披萨": 32}
# for item in dict_menu.items():
#     print(item, end=" ")
# print()
#
# dict_menu = {"汉堡": 15, "鸡翅": 10, "薯条": 6, "骨肉相连": 12, "披萨": 32}
# for key in dict_menu.keys():
#     print(key, end=" ")
# print()
#
# dict_menu = {"汉堡": 15, "鸡翅": 10, "薯条": 6, "骨肉相连": 12, "披萨": 32}
# for value in dict_menu.values():
#     print(value, end=" ")
# print()
#
# dict_menu = {"汉堡": 15, "鸡翅": 10, "薯条": 6, "骨肉相连": 12, "披萨": 32}
# for key, value in dict_menu.items():
#     print(key, value, end=" ")
# print()
#
# a = dict_menu.popitem()
# print(a)
# print(dict_menu)
#
# print(dict_menu.items())

# dicAreas = {"Russia": 1707.5, "Canada": 997.1, "China": 960.1}
# Is = sorted(dicAreas)
# print(Is)

# a = "I love , you"
# a = tuple(a)
# print(a)


# s = [1, 1, 2, 3, 4]
# s = set(s)
# print(s)

# list_a = [i for i in range(1, 101) if i % 3 == 0]
# print(list_a)
#
# list_rate = [57, 56, 57, 62, 69, 72, 75, 76, 74.3, 74]
# average_rate = sum(list_rate) / len(list_rate)
# print(average_rate)
#
# max_year = list_rate.index(max(list_rate)) + 2006
# print(max_year)


# def average_core(list_core):
#     return (sum(list_core) - min(list_core) - max(list_core)) / (len(list_core) - 2)
#
#
# core = {}
# core_012 = [90, 94, 97, 86, 85, 89, 88, 85]
# core_005 = [91, 91, 92, 98, 90, 96, 90, 95]
# core_108 = [96, 86, 97, 96, 87, 86, 86, 96]
# core_037 = [95, 95, 94, 93, 97, 98, 99, 95]
# core_066 = [95, 87, 94, 94, 93, 99, 96, 97]
# core_020 = [89, 97, 91, 95, 89, 94, 97, 92]
# core["012"] = average_core(core_012)
# core["005"] = average_core(core_005)
# core["108"] = average_core(core_108)
# core["037"] = average_core(core_037)
# core["066"] = average_core(core_066)
# core["020"] = average_core(core_020)
#
# print(core)
# core = [(x, y) for x, y in core.items()]
# core = sorted(core, key=lambda x: x[1], reverse=True)
# print(core)


class1 = {"李雷", "张玉", "王晓刚", "陈红静", "方向", "司马清"}
class2 = {"施然", "李芳芳", "刘潇", "孙一航", "方向", "黄煌"}
class3 = {"刘培良", "张玉", "施小冉", "陈红静", "方向", "司马清"}
class_num = len(class1 | class2 | class3)
num_3 = len(class1 & class2 & class3)
num_2 = len(class1 & class2) + len(class1 & class3) + len(class3 & class2)\
        - 2 * num_3
print("这个班一共有{}位同学没有选课".format(25 - class_num))
print("这个班一共有{}位同学选了2门".format(num_2))
print("这个班一共有{}位同学选了3门".format(num_3))
print("这个班一共有{}位同学选了1门".format(class_num - num_3 - num_2))

# import math
# a = 12
# b = 16
# c = 32
# gcd_abc = math.gcd(a, b, c)
# print(gcd_abc)
# multiple_a = a // gcd_abc
# multiple_b = b // gcd_abc
# multiple_c = c // gcd_abc
# print(multiple_a, multiple_b, multiple_c)
# mcm_abc = multiple_a * multiple_b * multiple_c * gcd_abc
# print(mcm_abc)
