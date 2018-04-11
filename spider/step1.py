from lxml import etree
import requests
from m_common import *
from bs4 import BeautifulSoup
import re



def gettext(url,code='utf-8'):
    r=requests.get(url,headers=fake_headers)
    r.raise_for_status()
    r.encoding=code
    return r.text


def soup(text):
    soup=BeautifulSoup(text,'html.parser')
    a = soup.findAll(text=re.compile('招生简章'))
    print(a)
    return a



def handletext(text):
    html=etree.HTML(text)
    url_list=html.xpath('//@href')
    # print(html_data)
    print(len(url_list))
    return url_list


def fixurl(url_list,url):
    list=[]
    for x in url_list:
        if x[:4]!='http':
            x=url+x
            list.append(x)
        else:
            list.append(x)
    return list

def rollurl(url):
    text = gettext(url)
    fixed_url = fixurl(handletext(text), url)




def handle_urllist(list):
    good_list1=[]
    bad_list=[]
    for x in list:
        try:
            text=gettext(x)
            if len(soup(text))==0:
                bad_list.append(x)
            else:
                good_list1.append(x)
                print(good_list1)
        except:
            continue
    print(good_list1)















def  main():
    url='http://grs.pku.edu.cn/'
    text=gettext(url)
    fixed_url=fixurl(handletext(text),url)
    handle_urllist(fixed_url)



main()