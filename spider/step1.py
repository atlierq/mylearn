from lxml import etree
import requests
from m_common import *
from bs4 import BeautifulSoup
import re
import copy
import jiebatest



def gettext(url,code='utf-8'):
    r=requests.get(url,headers=fake_headers,timeout=10)
    r.raise_for_status()
    r.encoding=code
    return r.text


def soup(text):

    soup=BeautifulSoup(text,'html.parser')
    a = soup.findAll(text=re.compile(r'.*(研究生|硕士生).*招生简章.*'))

    # b=copy.deepcopy(list(a))
    # print(b)
    #
    # for x in b:
    #
    #     if len(x)>30:
    #         a.remove(x)
    #     else:
    #         continue

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
            x=url.rstrip('/')+'/'+x.lstrip('/')
            list.append(x)
        else:
            list.append(x)
    return list

def rollurl(url):
    first_url='http://yz.bnu.edu.cn/'
    text = gettext(url)
    fixed_url = fixurl(handletext(text), first_url)
    return fixed_url

def handleMobileurl(listed):
    a=copy.deepcopy(listed)
    for x in listed:
        if 'mobile' in x:
            a.remove(x)
        else:
            continue
    return a


def handle_urllist(url_list):
    good_list1=[]
    good_list2=[]
    good_list3=[]
    bad_list=[]
    for x in url_list:
        try:
            text=gettext(x)
            if len(soup(text))==0:
                bad_list.append(x)
                print(rollurl(x))
                for url in rollurl(x):
                    text=gettext(url)
                    if len(soup(text))==0:
                        for url1 in rollurl(url):
                            text=gettext(url1)
                            if len(soup(text))==0:
                                pass
                            else:
                                good_list3.append(url1)



                    else:
                        good_list2.append(url)


            else:
                good_list1.append(x)
                print(good_list1)
        except:
            continue
    print('-------------------')
    # print(good_list3)
    # print(good_list2)
    # print(good_list1)
    a1=list(set(good_list1))
    a2=list(set(good_list2))
    a3=list(set(good_list3))
    fin_list1=handleMobileurl(a1)

    fin_list2=handleMobileurl(a2)

    fin_list3=handleMobileurl(a3)
    print('-------------------')
    # print(fin_list3)
    # print(fin_list2)
    # print(fin_list1)
    final=[x for l in [fin_list1,fin_list2,fin_list3] for x in l]
    print(final)
    return final




def  main():
    url='http://yz.bnu.edu.cn/'
    text=gettext(url)
    fixed_url=fixurl(handletext(text),url)
    fianl_list=handle_urllist(fixed_url)
    jiebatest.main(fianl_list)



main()