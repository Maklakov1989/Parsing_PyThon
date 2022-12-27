print(('*' * 25), 'Задание №1 к лекции № 2', ('*' * 25))
import requests
from lxml import html
from bs4 import BeautifulSoup
def parsing():
  headers = {
    "User_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0',
  }
  params = {
    'message': "",
  }
  url = 'https://lenta.ru/'
  link = requests.get(url, headers=headers, params=params)
  news = html.fromstring(link.text)
  news_list = news.xpath("//span[contains(@class,'card-mini__title')]/text()")[0: 10]
  news_time = news.xpath("//div[contains(@class,'card-mini__info')]/time/text()")[0: 10]
  news_link = news.xpath("//a[contains(@class, 'card-mini')]/@href")[0: 10]
  news_dict = dict(zip(news_list,zip(news_time,news_link)))
  print(news_dict)
parsing()

print(('*' * 25), 'Задание № вне плановое к лекции № 2', ('*' * 25))

def parsing_rbc():
  headers = {
    "User_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0',
  }
  url = 'https://www.rbc.ru/'
  link = requests.get(url, headers=headers)
  content = link.text
  soup = BeautifulSoup(content, 'html.parser')
  m = [el.getText() for el in soup.find_all('span', {'class': 'main__feed__title-wrap'})]
  m = [x.strip('\n              ') for x in m]
  m = [x.strip('\xa0') for x in m]
  l = [a.get('href') for a in soup.find_all('a', {'class': 'main__feed__link js-yandex-counter js-visited'})]
  news_dict = dict(zip(m, l))
  print(news_dict)

parsing_rbc()

