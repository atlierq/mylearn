# 2.2.4 生成器表达式
# symbols='@#$%^&*'
# # print([ord(x) for x in symbols])
# # print(list(filter(lambda c :c>40,map(ord,symbols))))
# # colors=['a','b','c']
# # sizes=[1,2]
# # t=[(color,size) for color in colors
# #                 for size in sizes]
# # print(t)
# #
# # a1=tuple(ord(x) for x in symbols)
# # print(a1)
# # print(type(a1))
#
# # colors=['red','blue','white']
# # sizes=['s','l','m']
# # for x in ('%s %s' %(c,s) for c in colors for s in sizes):
# #     print(x)
#
# #   _作占位符
# import os
# _,a=os.path.split(os.getcwd())
# print(a)
#
# # *rest可以拆分可迭代对象,*rest可以放在任何位置
# t=(1,2)
# print(*t)
# a,b,*rest=range(10)
# print(a,rest)
# print(a,*rest)
#
# #测试
# # print('{:15}|{:^9}|{:^9}'.format('','ds','s'))
#
# #namedtuple  创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字
# from collections import namedtuple
# City=namedtuple('City','name country population coordinates')
# tokyo=City('tokyo','JP',369.33,(1635,1122))
# # print(tokyo)
# # print(tokyo.name,tokyo.coordinates)
# # print(tokyo[-1])
#
# print(City._fields)
# latlong=namedtuple('latlong','lat long')
# a1=City('Delhi NCR', 'IN', 21.935, latlong(28.613889, 77.208889))
# delhi_data = ('Delhi NCR', 'IN', 21.935, latlong(28.613889, 77.208889))
# delhi=City._make(delhi_data)#等价于City(*delhi_data)
# print(delhi)
# a2=delhi._asdict()# _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。
# print(a2)
#
# # for key,value in delhi._asdict().items():
# #     print(key+':',value)


#2.3.5 作为不可变列表的元组
# a1=('a','b','c','d','a')
# a2=(1,2,3)
# b1=['a','b','c']
# b2=[1,2,3]
# print(a1.__add__(a2))
# print(b1.__iadd__(a1))#tuple不可以使用，等价于b1+=a1
# print(a1.__contains__('a'))
# print(a1.count('a'))
# print(a1.__getitem__(-1))
# print(a1.index('b'))#在 s 中找到元素 e 第一次出现的位置
# b1.insert(-1,'s')
# # print(b1)
# x=iter(a1)#使用iter()函数将Iterable变成Iterator
# print(x)
# for a in x:
#     print(a)
#from collections import Iterator
# print(isinstance(x,Iterator))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(sorted(a1))
# print(b1)
# b1.remove('b')#该方法没有返回值,so,不可以直接用print
# print(b1)
# a=list(range(5))
# print(a)
# print(a[:3])
# print(a[3:])
# print(a[1:4:2])
# print(a[2:])
# b=a.__getitem__(slice(1,3))
# print(b)

#2.42对对象进行切片
# invoice='''
# 0....5........................30......37..40..........51
# 1909 Pimoroni PiBrella          $17.50   3     $52.50
# 1489 6mm Tactile Switch x20     $4.95    2     $9.90
# 1510 Panavise Jr. - PV-201      $28.00   1     $28.00
# 1601 PiTFT Mini Kit 320x240     $34.95   1     $34.95
# '''
# line_items=invoice.split('\n')[2:]
# UNIT_PRICE = slice(40, 52)
# DESCRIPTION = slice(6, 40)
# a=slice(0,5)
# b=slice(30,37)
# # print(line_items)
# for item in line_items:
#     print(item[a],item[b])

#2.4.3 多维切片和省略
# 如果要得到 a[i, j] 的值，Python 会
# 调用 a.__getitem__(slice(i, j))
# a=list(range(5))
# b=a.__getitem__(slice(1,3))
# print(b)

#2.4.4 给切片赋值
# l=list(range(10))
# print(l)
# print(len(l))
# l[2:5]=[20,30]
# print(len(l))#注意l的长度变化
# print(l)
# del l[5:7]
# print(l)
# #如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代
# #对象。即便只有单独一个值，也要把它转换成可迭代的序列
# print("\n-------------------------\n")

#2.5 对序列使用+和*
# l=[1,2,3]
# print(l*5)
# print('asd'*3)
# board1=[['_']*3 for x in range(3)]#正确
# board2=[['_']*3]*3#错误
# #board3
# row1=['_']*3
# board3=[]
# for x in range(3):
#     board3.append(row1)#错误
# #board4
# board4=[]
# for x in range(3):
#     row2=['_']
#     board4.append(2)#正确，由于每次迭代中都新建了一个列表
# print("\n-------------------------\n")

#2.6 序列的增量赋值
# l=[1,2,3]
# print(id(l))
# l*=2
# print(id(l))
# t=(1,2,3)
# print(id(t))
# t*=2
# print(id(t))
# s='abc'
# print(id(s))
# s*=2
# print(id(s))

#一个谜题
# t=(1,2,[3,4])
# t[2] +=[5,6]
# print(t)
# print("\n-------------------------\n")


#2.7 list.sort方法和内置函数sorted
#list.sort 方法会就地排序列表,返回值为None

# fruits = ['grape', 'raspberry', 'apple', 'banana']
# a1=sorted(fruits)
# print(a1)
# print(fruits)
# a2=sorted(fruits,key=len,reverse=False)#key还可以是str.lower
# print(a2)
#
# fruits.sort()
# print(fruits)#使用这种方法为fruits自身进行排序
#
# print("\n-------------------------\n")

#2.8 用bisect来管理已排序的序列
# list1=[1,2,3,4,5,6,7,9,10]
# import bisect
# i=bisect.bisect(list1,7)#返回值为位置
# print(i)
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# for x in reversed(NEEDLES):
#     print(x)
#bisect 寻找数字位置

# import bisect
# import sys
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * ' |'
#         print(ROW_FMT.format(needle, position, offset))
#
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#         print('DEMO:', bisect_fn.__name__)
#         print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#         demo(bisect_fn)
# print("\n-------------------------\n")

#bisect插入数字

# import bisect
# import random
# size=7
# random.seed(129)
# my_list=[]
# for i in range(size):
#     new_item=random.randrange(size*2)
#     bisect.insort(my_list,new_item)
#     print('%2d->'%new_item,my_list)
#
# print("\n-------------------------\n")

#2.9 当列表不是首选时
#2.9.1 数组】
#适用于只包含数字的情况
# from array import array
# from random import random
#
#
# floats= array('d',(random() for x in range(100)))
# # print(floats[-1])
# # fp=open('floats.txt','wb')
# # floats.tofile(fp)
# # fp.close()
# # floats2=array('d')
# # fp=open('floats.txt','rb')
# # floats2.fromfile(fp,10**7)
# # fp.close()
# # print(floats2[-1])
# print(floats)
# print(floats.tolist())
# print(floats.typecode)
# a=array('d',sorted(floats))
# print(a)
#数组排序需要重新建立一个数组

#2.9.2 内存视图
# import array
# numbers = array.array('h', [-2, -1, 0, 1, 2])
# memv = memoryview(numbers)
# print(len(memv))
# memv_oct=memv.cast('B')
# print(memv_oct.tolist())

# 2.9.3 NumPy和SciPy
# import numpy
# a=numpy.arange(12)
# print(a)
# print(a.shape)
# a.shape=3,4
# print(a)
# print(a[:,1])#打印第二列
# print(a.transpose())#行列转换

# 示例 2-23 使用双向队列
# from collections import deque
# dq=deque(range(10),maxlen=(10))
# print(dq)
# dq.rotate(3)
# print(dq)
# dq.appendleft(100)
# print(dq)
# dq.extend([200,300])
# print(dq)
# print(dq.pop())
# #deque不能用sort排序


#（https://docs.python.org/3/howto/sorting.html）通过几个例子讲解了sorted 和 list.sort 的高级用法。