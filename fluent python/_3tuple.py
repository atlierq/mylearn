# symbols='@#$%^&*'
# print([ord(x) for x in symbols])
# print(list(filter(lambda c :c>40,map(ord,symbols))))
# colors=['a','b','c']
# sizes=[1,2]
# t=[(color,size) for color in colors
#                 for size in sizes]
# print(t)
#
# a1=tuple(ord(x) for x in symbols)
# print(a1)
# print(type(a1))

# colors=['red','blue','white']
# sizes=['s','l','m']
# for x in ('%s %s' %(c,s) for c in colors for s in sizes):
#     print(x)

#   _作占位符
import os
_,a=os.path.split(os.getcwd())
print(a)

# *rest可以拆分可迭代对象,*rest可以放在任何位置
t=(1,2)
print(*t)
a,b,*rest=range(10)
print(a,rest)
print(a,*rest)

#测试
# print('{:15}|{:^9}|{:^9}'.format('','ds','s'))

#namedtuple  创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字
from collections import namedtuple
City=namedtuple('City','name country population coordinates')
tokyo=City('tokyo','JP',369.33,(1635,1122))
# print(tokyo)
# print(tokyo.name,tokyo.coordinates)
# print(tokyo[-1])
print(City._fields)
latlong=namedtuple('latlong','lat long')
a1=City('Delhi NCR', 'IN', 21.935, latlong(28.613889, 77.208889))
delhi_data = ('Delhi NCR', 'IN', 21.935, latlong(28.613889, 77.208889))
delhi=City._make(delhi_data)#等价于City(*delhi_data)
print(delhi)
a2=delhi._asdict()# _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。
print(a2)
# for key,value in delhi._asdict().items():
#     print(key+':',value)