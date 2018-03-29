#http://yz.chsi.com.cn/sch/search.do?start=0
import requests
from bs4 import BeautifulSoup
from m_common import *
import pymysql
import traceback

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
            i=0
            while a.split('/')[2][-6:]!='edu.cn':
                i+=1
                a = Ssoup.findAll('li', attrs={'class': 'b_algo'})[i].a.attrs['href']


            school_url_list.update({x:a})

        except:
            continue
    return school_url_list

def mysqlText(list):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='school', charset="utf8")
    cur=conn.cursor()
    sqlc='''create table school(
    id int(11) NOT NULL auto_increment PRIMARY KEY ,
    school_name VARCHAR (255) NOT NULL ,
    school_url VARCHAR (255) NOT NULL )DEFAULT charset=utf8;
    '''
    try:
        cur.execute(sqlc)
        conn.commit()
        print('ok')
    except:
        traceback.print_exc()

    for x in list:
        sqla='''insert into school(school_name,school_url) VALUES (%s,%s);'''
        try:
            cur.execute(sqla,(x,list[x]))
            conn.commit()
            print('ok')
        except:
            traceback.print_exc()

    conn.commit()
    cur.close()




def main():
    url = 'http://yz.chsi.com.cn/sch/search.do?ssdm=&yxls=&b985=1&b211=1'
    html=getHtmlText(url)
    Schlist=[]
    getSchoollist(html,Schlist)
    new_list=getSchoolurl(Schlist)
    mysqlText(new_list)




main()