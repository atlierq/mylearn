import requests
import re
from bs4 import BeautifulSoup
import traceback


def gethtmltext(url,code='utf-8'):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=code
        return r.text
    except:
        return "sd"

def getstocklist(html,lis):
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lis.append(re.findall(r's[hz]\d{6}',href)[0])#"[0] #会将不符合正则表达式的去除"
        except:
            continue

def getbaidu(lis3,html1,fpath):
    count=0
    for x in lis3:
        url=html1 + x + ".html"
        print(url)
        html=gethtmltext(url)
        try:
            if html=='':
                continue
            lis1={}
            soup=BeautifulSoup(html,'html.parser')
            stockinfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockinfo.find_all(attrs={'class':'bets-name'})[0]

            lis1.update({'名称':name.text.split()[0]})
            print(lis1)

            keylist=stockinfo.find_all('dt')
            vallist=stockinfo.find_all('dd')
            for i in range(len(keylist)):
                key=keylist[i].text
                val=vallist[i].text
                lis1[key]=val

            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(lis1)+'\n')
                count=count+1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lis3)),end='')

        except:
            count = count + 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(lis3)), end='')
            traceback.print_exc()




def main():
    baidustock="https://gupiao.baidu.com/stock/"
    dongfangstock="http://quote.eastmoney.com/stocklist.html"
    path1="d://baidu.txt"
    infolist=[]
    html=gethtmltext(dongfangstock,'GB2312')
    getstocklist(html,infolist)
    getbaidu(infolist,baidustock,path1)




main()


