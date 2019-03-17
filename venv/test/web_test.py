import requests
from bs4 import BeautifulSoup

url = "https://tieba.baidu.com/f?kw=%E9%9B%80%E9%AD%82&fr=index&fp=0&ie=utf-8"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
ass = soup.find_all('a', class_='j_th_tit')
for a in ass:
    print("https://tieba.baidu.com" + a['href'])
