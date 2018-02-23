import requests
import re
import json
from m_common import *
import urllib.parse as urlparse
import urllib.request
import os

LIMIT=100

class Board:
    def __init__(self, title, pins):
        self.title = title
        self.pins = pins
        self.pin_count = len(pins)

class Pin:
    host = 'http://img.hb.aicdn.com/'

    def __init__(self, pin_json):
        img_file = pin_json['file']
        self.id = str(pin_json['pin_id'])
        self.url = urlparse.urljoin(self.host, img_file['key'])
        self.ext = img_file['type'].split('/')[-1]



def construct_url(url,**params):
    para_str= urlparse.urlencode(params)
    return url + '?' + para_str



def getHTML(url,code='utf-8'):
    r=requests.get(url,fake_headers)
    r.raise_for_status()
    r.encoding=code
    return r.text


def getjson_data(url,**params):
    url1=construct_url(url,**params)
    html=getHTML(url1)
    json_string = re.findall(r'app.page\["board"\] = (.*?});', html)
    json_data = json.loads(json_string[0])
    return json_data


def extract_board(url):
    try:
        json_data=getjson_data(url,limit=LIMIT)
        title=json_data['title']
        pin_list=json_data['pins']
        pin_count=json_data['pin_count']
        print(pin_count)
        pin_count-=len(pin_list)
        while pin_count >0:
            json_data=getjson_data(url,limit=LIMIT,max=pin_list[-1]['pin_id'])
            pins=json_data['pins']
            pin_list +=pins
            pin_count-=len(pins)
        some_thing=list(map(Pin, pin_list))
        return Board(title,some_thing )
    except:
        print('something happended')

def huaban_board_download(url,s_path):
    urllib.request.urlretrieve(url,s_path)



def main():
    url='http://huaban.com/boards/41233035/'
    board=extract_board(url)
    print(board.title)
    os.mkdir('d:\\image\\%s'%board.title)
    # path='D:\image\\' + board.title+'\\'+x.id
    # print(path)
    for x in board.pins:
        # path = 'D:\\image\\' + board.title + '\\'+x.id+'.'+x.ext
        path='d:\\image\\%s\\%s.%s'%(board.title,x.id,x.ext)
        huaban_board_download(x.url,path)
        # print(path)
        # print(x.url,x.id)
        # D:\image

main()
