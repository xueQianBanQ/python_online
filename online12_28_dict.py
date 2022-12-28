
##################################字典
"""
scores = {"张三": 90, "李四": 99}
print(scores, type(scores))
scores = dict(张三 = 90, 李四 = 99)
print(scores, type(scores))
"""
""" 
scores = {"张三": 90, "李四": 99}
print(scores["张三"])
#print(scores["bit"])#KeyError: 'bit'
print(scores.get("张三"))
print(scores.get("bit"))#None
print(scores.get("bit", False))#如果不存在，返回False (可自己设定)
"""
"""
scores = {"张三": 90, "李四": 99}
scores["王五"] = 60#增
print(scores)
scores["张三"] = 100#改
print(scores)
del scores["王五"]#删
print(scores)
scores.clear()#清
print(scores)
"""
"""
scores = {"张三": 90, "李四": 99}
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))
values = scores.values()
print(values, type(values), list(values))
items = scores.items()
print(items)
print(type(items))
print(list(items))#元组
"""
"""
scores = {"张三": 90, "李四": 99}
for key in scores:#获取的是键
    print(key, scores[key], scores.get(key))
"""
items = ["fruit", "book", "other"]
prices = [98, 90, 80]
nemu = {i.upper():j   for i, j in zip(items, prices)}
print(nemu)
