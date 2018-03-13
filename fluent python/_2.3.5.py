#作为不可变列表的元组
a1=('a','b','c','d','a')
a2=(1,2,3)
b1=['a','b','c']
b2=[1,2,3]
# print(a1.__add__(a2))
# print(b1.__iadd__(a1))#tuple不可以使用，等价于b1+=a1
# print(a1.__contains__('a'))
# print(a1.count('a'))
# print(a1.__getitem__(-1))
# print(a1.index('b'))#在 s 中找到元素 e 第一次出现的位置
b1.insert(-1,'s')
# print(b1)
x=iter(a1)#使用iter()函数将Iterable变成Iterator
# print(x)
# for a in x:
#     print(a)
from collections import Iterator
# print(isinstance(x,Iterator))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(sorted(a1))
print(b1)
b1.remove('b')#该方法没有返回值,so,不可以直接用print
print(b1)