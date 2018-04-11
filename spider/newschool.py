import pymysql
import requests
from lxml import etree
from m_common import *
from bs4 import BeautifulSoup
import re


def getFROMsql():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='school', charset="utf8")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM school.school;')
    results = cursor.fetchall()
    result = list(results)
    print(result)

    return result

def gethtml(url,code='utf-8'):
    r=requests.get(url,headers=fake_headers,timeout=10)
    if r.status_code==200:
        pass
    else:
        print('something wrong')
    r.encoding=code
    return r.text


def getsoup(text,origin_url,dict,school,none_list):
    soup=BeautifulSoup(text,'html.parser')

    a=soup.findAll(text=re.compile('硕士招生|招生信息|学历硕士|统考硕士'))

    list=[]
    for x in a:
        try:
            new_url=x.parent.attrs['href']
        except:
            continue

        if new_url[:4]!='http':
            new_url = origin_url.rstrip('/') + '/' + new_url.lstrip('/')
            list.append(new_url)
        else:
            list.append(new_url)
    if len(list)==0:
        none_list.update({school[1]:school[2]})

    dict[school[1]]=list


def handlenone(none_list,dict):
    test_dict={}
    for school in none_list:
        text=gethtml(none_list[school])
        soup=BeautifulSoup(text,'html.parser')
        a=soup.findAll(text=re.compile('学历硕士|硕士研究生|研究生招生|硕士生招生'))
        list = []
        for x in a:
            try:
                new_url = x.parent.attrs['href']
            except:
                continue
            if new_url[:4] != 'http':
                new_url = none_list[school].rstrip('/') + '/' + new_url.lstrip('/')
                list.append(new_url)
            else:
                list.append(new_url)
        test_dict.update({school:list})
        dict[school] = list
    print('test_dict={}'.format(test_dict))

def main():
    s_list=[]
    first_list=getFROMsql()
    m_dict={}
    none_list = {}
    for x in first_list:
        try:
            url=x[2]
            text=gethtml(url)
            m_dict.update({x[1]:[]})
            getsoup(text,url,m_dict,x,none_list)
        except:
            print(x)
            continue
    # print(m_dict)
    print(none_list)
    handlenone(none_list,m_dict)
    print(m_dict)







main()