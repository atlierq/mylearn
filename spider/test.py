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

def main():
    getFROMsql()



main()