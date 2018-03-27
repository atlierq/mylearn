#http://yz.chsi.com.cn/sch/search.do?start=0
import requests
from bs4 import BeautifulSoup
from m_common import *
import re

def getHtmlText(url,code='utf-8'):
    r=requests.get(url,headers=fake_headers,timeout=10)
    r.raise_for_status()
    r.encoding=code
    print(r.status_code)
    return r.text

def getSchoollist(html,list):
    soup=BeautifulSoup(html,'html.parser')
    a=soup.findAll('tr')
    for x in a[1:]:
        # print(x.td.a.string.strip())
        list.append(x.td.a.string.strip())
    print(list)


def getSchoolurl(list):
    url='https://cn.bing.com/search?q='
    school_url_list={}
    for x in list:
        url1=url+x+'研究生招生网'
        try:
            Stext=getHtmlText(url1,code='utf-8')
            Ssoup=BeautifulSoup(Stext,'html.parser')
            a=Ssoup.findAll('li',attrs={'class':'b_algo'})[0].a.attrs['href']

            while a.split('/')[2][-6:]!='edu.cn':
                i=1
                a = Ssoup.findAll('li', attrs={'class': 'b_algo'})[i].a.attrs['href']
                i=i+1
            school_url_list.update({x:a})
        except:
            continue
    print(school_url_list)



def main():
    url = 'http://yz.chsi.com.cn/sch/search.do?ssdm=&yxls=&b985=1&b211=1'
    html=getHtmlText(url)
    Schlist=[]
    getSchoollist(html,Schlist)
    getSchoolurl(Schlist)




main()