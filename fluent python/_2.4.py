a=list(range(5))
print(a)
# print(a[:3])
# print(a[3:])
# print(a[1:4:2])
print(a[2:])
# b=a.__getitem__(slice(1,3))
# print(b)

#2.42对对象进行切片
invoice='''
0....5........................30......37..40..........51
1909 Pimoroni PiBrella          $17.50   3     $52.50
1489 6mm Tactile Switch x20     $4.95    2     $9.90
1510 Panavise Jr. - PV-201      $28.00   1     $28.00
1601 PiTFT Mini Kit 320x240     $34.95   1     $34.95
'''
line_items=invoice.split('\n')[2:]
UNIT_PRICE = slice(40, 52)
DESCRIPTION = slice(6, 40)
a=slice(0,5)
b=slice(30,37)
# print(line_items)
for item in line_items:
    print(item[a],item[b])

#2.4.3 多维切片和省略
# 如果要得到 a[i, j] 的值，Python 会
# 调用 a.__getitem__(slice(i, j))
a=list(range(5))
b=a.__getitem__(slice(1,3))
print(b)

#2.4.4 给切片赋值
l=list(range(10))
print(l)
print(len(l))
l[2:5]=[20,30]
print(len(l))#注意l的长度变化
print(l)
del l[5:7]
print(l)
#如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代
#对象。即便只有单独一个值，也要把它转换成可迭代的序列
print("\n-------------------------\n")

#2.5 对序列使用+和*
l=[1,2,3]
print(l*5)
print('asd'*3)
board1=[['_']*3 for x in range(3)]#正确
board2=[['_']*3]*3#错误
#board3
row1=['_']*3
board3=[]
for x in range(3):
    board3.append(row1)#错误
#board4
board4=[]
for x in range(3):
    row2=['_']
    board4.append(2)#正确，由于每次迭代中都新建了一个列表
print("\n-------------------------\n")

#2.6 序列的增量赋值
l=[1,2,3]
print(id(l))
l*=2
print(id(l))
t=(1,2,3)
print(id(t))
t*=2
print(id(t))
s='abc'
print(id(s))
s*=2
print(id(s))

#一个谜题
# t=(1,2,[3,4])
# t[2] +=[5,6]
# print(t)
print("\n-------------------------\n")


#2.7 list.sort方法和内置函数sorted
#list.sort 方法会就地排序列表,返回值为None
fruits = ['grape', 'raspberry', 'apple', 'banana']
a1=sorted(fruits)
print(a1)
print(fruits)
a2=sorted(fruits,key=len,reverse=False)#key还可以是str.lower
print(a2)

fruits.sort()
print(fruits)#使用这种方法为fruits自身进行排序

print("\n-------------------------\n")

#2.8 用bisect来管理已排序的序列
list1=[1,2,3,4,5,6,7,9,10]
import bisect
i=bisect.bisect(list1,7)#返回值为位置
print(i)
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
for x in reversed(NEEDLES):
    print(x)
#bisect 寻找数字位置
import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
        print('DEMO:', bisect_fn.__name__)
        print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
        demo(bisect_fn)
print("\n-------------------------\n")

#bisect插入数字
import bisect
import random
size=7
random.seed(129)
my_list=[]
for i in range(size):
    new_item=random.randrange(size*2)
    bisect.insort(my_list,new_item)
    print('%2d->'%new_item,my_list)





