#https://steamcn.com/f161-
import requests

from bs4 import BeautifulSoup


def getHTMLtext(url,code='utf-8'):
    kv = {'user-agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=code
    return r.text

def HTMLparser(html,lis):
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a',{'class':'s xst'})
    for i in a:
        try:
            href=i.attrs['href']
            info=i.string
            lis.append([info,href])
            # print(lis)
        except:
            continue


def listHTML(lis):
    tplt = "{:<3}{:30}{:<10}"
    print(tplt.format("序号", "info", "链接", chr(12288)))
    count=0
    for x in lis:
        count=count+1
        print(tplt.format(count,x[0]+'  ','https://steamcn.com/'+x[1], chr(12288)))


def main():
    first_url='https://steamcn.com/f161-'
    num=5
    infolist=[]
    for x in range(num):
        try:
            x1=x+1
            url=first_url+str(x1)
            html=getHTMLtext(url)
            HTMLparser(html,infolist)
        except:
            continue
    listHTML(infolist)

main()





