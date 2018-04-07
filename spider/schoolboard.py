import pymysql
import requests
from lxml import etree
from m_common import *

def gettext(url,url1,code='utf-8'):
    urllist=[]
    try:
        r=requests.get(url,headers=fake_headers,timeout=10)
        r.raise_for_status()
        print(r.status_code)
        r.encoding=code
        urllist.append(url)
        return r.text




    except:
        # print(url1,url.strip('/'))
        url=url1+url.strip('/')
        # print(url)
        gettext(url,url1)






def doxpath(html,Route):
    # print(type(html))
    html1 = etree.HTML(html)
    html_data = html1.xpath(Route)
    return html_data



def getFROMsql():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='school', charset="utf8")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM school.school;')
    results = cursor.fetchall()
    result = list(results)
    print(result)
    return result


def getendurl(dict,x):
    l=len(dict[x[1]])
    html= gettext(x[2],x[2])

    i=0
    while l>=1:
        print(dict[x[1]][i]+'/@href')
        aurl=doxpath(html,dict[x[1]][i]+'/@href')
        print(aurl)
        i+=1
        l-=1
        # print([aurl[0],x[2]])
        html=gettext(aurl[0],x[2])
        # print(html)




ALL_route={'北京大学':['/html/body/div[1]/div[2]/ul/li[2]/a','//*[@id="left_menu"]/ul/li[2]/a'],
           '中国人民大学':['//*[@id="nav0"]/a'],
           '清华大学':['//*[@id="index_all"]/div[1]/div[3]/ul/li[3]/a','//*[@id="index_all"]/div[2]/div[1]/div/ul/li[1]/a'],#不行
           '北京航空航天大学':['/html/body/div[1]/div/ul/li[3]/a'],#不行
           '北京理工大学':['//*[@id="nav"]/li[3]/div/dl/dd[2]/a'],
           '中国农业大学':['//*//td/div/a[@title="硕士招生"]'],
           '北京师范大学':['//*[@id="bs-example-navbar-collapse-1"]/ul/li[1]/a']        ,
           '中央民族大学':[]
           }

def main():
    _1list=getFROMsql()
    print(len(_1list))
    getendurl(ALL_route,_1list[0])





main()
