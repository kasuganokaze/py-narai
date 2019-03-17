import requests
from bs4 import BeautifulSoup
import json

url = "https://tieba.baidu.com/f?kw=%E9%9B%80%E9%AD%82&fr=index&fp=0&ie=utf-8"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
ass = soup.find_all('a', class_='j_th_tit')
for a in ass:
    print("https://tieba.baidu.com" + a['href'])

url = 'https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?sign=&data=%7B%22itemNumId%22%3A%22577284665556%22%7D%27'
page = requests.get(url)
result_json = json.loads(page.text)
print(result_json['data'])
