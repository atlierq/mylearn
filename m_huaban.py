import requests
from m_common import *
import re
import json
from bs4 import BeautifulSoup

s_url="http://huaban.com/boards/13840182/?limit=100&max=119336732"

r=requests.get(s_url,fake_headers)
# print(r.status_code)
# print(r.encoding)
# print(r.headers)
html=r.text
# print(html)
json_string=re.findall( r'app.page\["board"\] = (.*?});',html)
# print(json_string)
json_data=json.loads(json_string[0])
print(json_data)
print(json_data['pins'])

# print(json_data)
# title = json_data['title']
# pin_count = json_data['pin_count']
# print(title)
# print(pin_count)
# print(b)
# print(b['pins'])
# print(b['pins'])
#
# a=json_data['pins'][-1]['pin_id']
# print(a)
# list=[]
# for x in b['pins']:
#     # print(x['pin_id'])
#     list.append(x['pin_id'])
# print(len(list))
# print(list)



# print(text)
# soup=BeautifulSoup(text,'html.parser')
# print(soup.prettify())
# m=soup.findAll('pin_id')
# print(m)