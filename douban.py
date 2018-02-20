# https://movie.douban.com/subject/26575103/comments?start=40
import requests
from bs4 import BeautifulSoup
import pymysql
import traceback
import re
# ×½Ñý¼Ç


def getHTMlText(url,code='utf-8'):
    kv = {'user-agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=code
    return r.text

def soupText(html,mlist):
    list1 = []
    list2 = []
    soup=BeautifulSoup(html,'html.parser')
    a=soup.findAll('div',{'class':'avatar'})
    # re_star=re.compile(r'(allstar)([\d]*)( rating)')
    b=soup.findAll('span',{'class':'comment-info'})
    for x in b:
        b1=x.findAll('span')[1]
        # b1.attrs['class'][0].split('r')[-1]
        list2.append((int(b1.attrs['class'][0].split('r')[-1])/10))

    # print(len(b))

    for x in a:
        usertitle=x.a.attrs['title']
        userhref=x.a.attrs['href']
        list1.append([usertitle,userhref])


    for m in range(len(list1)):
        mlist.append([list1[m][0],list1[m][1],list2[m]])

mysql
def mysqlText(mlist):
    # count=0
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Lj18119929389', db='douban', charset="utf8")
    cur = conn.cursor()
    sqlc = '''create table movie(
                id int(11) not null auto_increment primary key,
                name varchar (255) not null,
                u_star int(11) not null,
                u_url varchar (255) not null)DEFAULT  CHARSET=utf8;
                '''
#
    try:
        cur.execute(sqlc)
        # print(a)
        conn.commit()
        print('ok')
    except:
        print('wrong1')
    for x in mlist:
        # count =count+1
        sqla = '''insert into  movie(name,u_url,u_star) values(%s,%s,%s);'''
        try:
            cur.execute(sqla,(x[0],x[1],x[2]))
            conn.commit()
            print('ok')
        except:
            print('wrong2')
            # traceback.print_exc()
    conn.commit()
    cur.close()
    conn.close()



def main():

    start_url="https://movie.douban.com/subject/26575103/comments?start="
    list=[]
    for x in range(5):
        r=x*20
        url=start_url+str(r)
        html=getHTMlText(url)
        soupText(html,list)
    print(list)
    print(mysqlText(list))


main()
