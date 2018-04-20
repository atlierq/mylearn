import jieba
import requests
from bs4 import BeautifulSoup
import re

def gettext(url):
    r=requests.get(url)
    r.encoding='utf-8'
    return r.text

def fengci(sge):
    s=jieba.cut_for_search(sge)
    return list(s)


def souptext(text):
    soup=BeautifulSoup(text,'html.parser')
    a=soup.findAll('a')
    return a

def handlestring(list,list1):
    s=r'.*[a-zA-Z]+.*'
    for x in list:
        if not(re.match(s,str(x.string))):
            a=fengci(str(x.string))
            if hexing(a):
                # print([x.string,x.attrs['href']])
                if [x.string,x.attrs['href']] not in list1:
                    list1.append([x.string,x.attrs['href']])

                # print(list1)
            else:
                continue
        else:
            continue

    return list1






def hexing(list):
    list1=['招生简章','2018']#必须有的词
    list2=['硕士','研究生','硕士生']#必须有其中一个
    list3=['博士','管理','卫生','法律','心理','港澳台','艺术','智能','工程']

    if len(set(list3)&set(list))==0:
        if len(set(list2)&set(list))>=1:
            if len(set(list1) & set(list))==len(list1):
                return True
            else:
                return False
        else:
            return False
    else:
        return False






def main(a):
    list=[]
    # a=['http://yz.tsinghua.edu.cn/publish/yjszs/8549/index.html']
    # a=['http://yz.tsinghua.edu.cn//publish/yjszs/8550/2017/20170927095143586235746/20170927095143586235746_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8563/2016/20160905082235466929153/20160905082235466929153_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8546/2017/20170821093548376210482/20170821093548376210482_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8549/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8562/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8563/2017/20170330100243592699221/20170330100243592699221_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8550/2018/20180309133444081925352/20180309133444081925352_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8550/index_9.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8558/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8546/2017/20171030091737912441274/20171030091737912441274_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8545/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8546/index_9.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8553/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8549/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8562/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8563/2017/20170330100243592699221/20170330100243592699221_.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8558/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8545/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8553/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8562/index.html', 'http://yz.tsinghua.edu.cn//publish/yjszs/8563/2017/20170330100243592699221/20170330100243592699221_.html']
    for x in a:
        try:
            final=handlestring(souptext(gettext(x)),list)

        except:
            continue

    print(final)



