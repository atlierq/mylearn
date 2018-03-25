# 字典这个数据结构活跃在所有 Python 程序的背后，即便你的源码里并没有直接用到它。
#                                                     ——A. M. Kuchling
#3.1 泛映射类型
# s=set('2313')
# s1=frozenset('sdfsdf')
# print(s)
# for x in s:
#     print(x)
# #由于set是可变的，因此不存在hash值,而frozenset是不可变的
# print(hash(s1))


#创建字典的不同方式
# a=dict(one=1,two=2,three=3)
# b={'one':1,'two':2,'three':3}#感觉这个最常用
# c=dict(zip(['one','two','three'],[1,2,3]))
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})
# print(a==b==c==d==e)

#3.2字典推导
# DTAL_CODES=[(86, 'China'),(91, 'India'),(1, 'United States'),(62, 'Indonesia'),(55, 'Brazil'),(92, 'Pakistan'),(880, 'Bangladesh'),(234, 'Nigeria'),(7, 'Russia'), (81, 'Japan')]
# print(type(DTAL_CODES))
# country_code = {country: code for code, country in DTAL_CODES}
# print(country_code)
# country_code1={x:y.upper() for y,x in country_code.items() if x <60}
# #d.items() 返回 d 里所有的键值对
# print(country_code1)
# # print(country_code.keys())


# 3.3 常见的映射方法
# new_dict={'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
# print(new_dict.get('chin','can\'t find'))#d.get(k, default) 来代替 d[k]会更高效
#d.update(m,[**kargs])方法处理参数m时，会先检查是否有keys方法，把m当做映射对象来处理，否则会把m当作包含键值对元素的迭代器

#用setdefault处理找不到的键
# import sys
# import re
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open('a.txt', encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):#(1)
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start()+1
#             location = (line_no, column_no)
# # 这其实是一种很不好的实现，这样写只是为了证明论点
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
# # 以字母顺序打印出结果
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
# # (1)enumerate是内置函数，可以获取索引值，emumerate(m,1)表示索引起始值为1
# import re
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open('a.txt', encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):#(1)
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start()+1
#             location = (line_no, column_no)
# # 这其实是一种很不好的实现，这样写只是为了证明论点
#             index.setdefault(word, []).append(location)
#             print(index)
# # 以字母顺序打印出结果
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
#d.setdefault(k,[default])
#若字典里有键k，则把它对应的值设置为 default，然后返回这个
# 值；若无，则让 d[k]=default，然后返回 default
#使用setfault更加高效，只需要一次查询

#3.4　映射的弹性键查询
# 3.4.1defaultdict
#index = collections.defaultdict(list)
#index[word].append(location)
#list 为default_factory，此方法只能在__getitem__中被调用，所有这一切背后的功臣其实是特殊方法 __missing__。它会在
#defaultdict 遇到找不到的键的时候调用 default_factory

#3.4.2　特殊方法__missing__
# class StrKeyDict0(dict): #➊
#     def __missing__(self, key):
#         if isinstance(key, str):# ➋如果找不到的键本身就是字符串，那就抛出 KeyError 异常。
#             raise KeyError(key)
#         return self[str(key)] #➌相当于再给一次机会
#     def get(self, key, default=None):
#         try:
#             return self[key] #➍使用get方法时也可以使用使用__missing__的方法
#         except KeyError:
#             return default #➎
# def __contains__(self, key):
#     return key in self.keys() or str(key) in self.keys() #➏在k in d 这个操作会调用到他


# 3.5　字典的变种
#collections.OrderedDict 这个类型在添加键时会保持顺序，因此迭代顺序会保持一致
#d.popitem会默认删除最后一个元素
# collections.ChainMap 没看懂
#collections.Counter
# import collections
# ct=collections.Counter('fhjaskdjfhakjshnk')
# print(ct)
# ct.update('dsafdsafgasdgwe')
# print(ct.most_common(2))#most_common([n]) 会按照次序返回映射里最常见的 n 个键和它们的计数
# collections.UserDict
#，UserDict 是让用户继承写子类的


# 3.6　子类化UserDict
#####################################################
# 没看懂

#3.7　不可变映射类型
# from types import MappingProxyType
# d={1:'a'}
# d_proxy=MappingProxyType(d)
# print(d_proxy)
# print(d_proxy[1])
# # d_proxy[2]='x'#会报错，由于d_proxy不可以修改
# d[2]='p'
# print(d_proxy)#d_proxy 是动态的，也就是说对 d 所做的任何改动都会反馈到它上面。


#3.8集合论
#集合可以去重
# l=['a','b','c','b','a']
# m=['a','b','d','f']
# l1=set(l)
# print(l1)
# print(list(l1))
# #集合可以实现交集a&b，合集a|b，差集a-b等操作
# found=len(set(l).intersection(set(m)))#交集的另一种写法
# print(found)

#3.8.1　集合字面量
# s1={}
# s2=set()
# print(type(s1),type(s2))

# from dis import dis
# dis('{1}')
# print('--------------------------')
# dis('set([1])')

# from unicodedata import name#从 unicodedata 模块里导入 name 函数，用以获取字符的名字。
# a={chr(i) for i in range(32,256) if 'SIGN' in name (chr(i),'')}
# print(a)
# a1={1,2,3,4}
# a2={1,2}
# print(a2<a1)
# print(a1.__len__())
# a=a1.__iter__()

