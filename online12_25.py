#print("hello")
#print('hello\nworld')
#print('hello\rworld')
#print('hello\bworld')
#print('hello \'world\'')
#print('hello \\ world')
#print(r'hello\nworld')#注意最后一个不能是一个\
#import keyword
#print(keyword.kwlist)

#name = '玛利亚'
#print(name)
#print("标识", id(name))
#print('类型', type(name))


#a = 90
#b = 0
#c = -70
#print(a,type(a), end=' ')
#print(b,type(b))
#3print(c, type(c))


'''print('十进制', 456)
print('二进制', 0b1001)
print('八进制', 0o374)
print('十六进制', 0x123)'''

'''
n1 = 1.1
n2 = 2.2
print(n1+n2) #3.3000000000000003

from decimal import Decimal
print(Decimal(n1) + Decimal(n2))#不对， 还不能使用变量说的
print(Decimal('1.1') + Decimal('2.2'))
'''
'''
name = '张三'
age = 20
print('今年', age, '岁')
print(name + '今年'+ str(age) + '岁')
'''


present = input('大圣想要啥？')
print(present, type(present))
