import requests
from lxml import html
from pymongo import MongoClient
from bs4 import BeautifulSoup
from datetime import date

print(('*' * 25), 'Задание №1 к лекции № 4', ('*' * 25))
def parsing():
  headers = {
    "User_agent": (
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/106.0.0.0 YaBrowser/22.11.3.818 '
      'Yowser/2.5 Safari/537.36'
    ),
  }
  url = 'https://lenta.ru/'
  link = requests.get(url, headers=headers)
  news = html.fromstring(link.text)
  news_list = news.xpath("//span[contains(@class,'card-mini__title')]/text()")[0: 15]
  news_time = news.xpath("//div[contains(@class,'card-mini__info')]/time/text()")[0: 15]
  news_link = news.xpath("//a[contains(@class, 'card-mini')]/@href")[0: 15]
  client = MongoClient('localhost', 27017)
  db = client.db_news
  db.news
  db.news.drop()
  now = date.today()
  d = {f'Lenta.ru публикует {now}': [{'Message': m, 'Time': t, 'link': url + l} for m, t, l
                    in zip(news_list, news_time, news_link)]}
  db.news.insert_one(d)
  for document in db.news.find():
    print(document)

if __name__ == '__main__':
    parsing()

print(('*' * 25), 'Задание № вне плановое к лекции № 4', ('*' * 25))

def parsing_rbc():
  headers = {
    "User_agent": (
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/106.0.0.0 YaBrowser/22.11.3.818 '
      'Yowser/2.5 Safari/537.36'
    ),
  }
  url_rbk = 'https://www.rbc.ru/'

  link = requests.get(url_rbk, headers=headers)
  content = link.text
  soup = BeautifulSoup(content, 'html.parser')
  mes = [el.getText() for el in
         soup.find_all('span', {'class': 'main__feed__title-wrap'})]
  mes = [x.strip('\n              ')
         for x in mes]
  mes = [x.strip('\xa0') for x in mes]
  links = [a.get('href') for a
           in soup.find_all('a', {'class':
                                    'main__feed__link js-yandex-counter js-visited'
                                  })]
  client = MongoClient('localhost', 27017)
  db = client.db_news
  db.news
  now = date.today()
  data = {f'rbc.ru публикует {now}': [{'Message': m, 'link': url_rbk + l} for m, l
                    in zip(mes, links)]}
  db.news.insert_one(data)
  for document in db.news.find():
    print(document)

if __name__ == '__main__':
    parsing_rbc()
