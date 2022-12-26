print(('*' * 25), 'Задание №1 к лекции № 2', ('*' * 25))
import requests
from lxml import html
from bs4 import BeautifulSoup
def parsing():
  headers = {
    "User_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.818 Yowser/2.5 Safari/537.36',
  }
  url = 'https://www.rabota.ru/vacancy/?query=python&sort=relevance&page=1'
  link = requests.get(url, headers=headers)
  content = link.text
  vacancyes_dict = {}
  soup = BeautifulSoup(content, 'html.parser')
  salary = soup.find_all('div', {'class':'vacancy-preview-card__salary'})
  v = [el.getText() for el in soup.find_all('a', {'class':'vacancy-preview-card__title_border'})]
  v = [x.strip('\n              ') for x in v]
  s = [el.getText() for el in soup.find_all('div', {'class':'vacancy-preview-card__salary'})]
  s = [x.strip('\n              ') for x in s]
  s = [x.replace('\xa0', ' ') for x in s]
  news_dict = dict(zip(v, s))
  print(news_dict)
parsing()