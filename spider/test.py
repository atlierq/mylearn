import requests
from bs4 import BeautifulSoup
url='https://cn.bing.com/search?q=%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%94%9F%E9%99%A2'
r=requests.get(url)
html=r.text
soup=BeautifulSoup(html,'html.parser')
a=soup.findAll('li',attrs={'class':'b_algo'})[0].a.attrs['href']
print(a)