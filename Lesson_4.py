import requests
from lxml import html
from pymongo import MongoClient
import json

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
  client = MongoClient('localhost', 27017)
  db = client.db_news
  db.news
  db.news.drop()
  url = 'https://lenta.ru/'
  link = requests.get(url, headers=headers)
  news = html.fromstring(link.text)
  news_list = news.xpath("//span[contains(@class,'card-mini__title')]/text()")[0: 15]
  news_time = news.xpath("//div[contains(@class,'card-mini__info')]/time/text()")[0: 15]
  news_link = news.xpath("//a[contains(@class, 'card-mini')]/@href")[0: 15]
  d = {'Lenta.ru': [{'Message': m, 'Time': t, 'link': url + l} for m, t, l
                    in zip(news_list, news_time, news_link)]}
  #print(json.dumps(d, indent=4))
  db.news.insert_one(d)
  # for item in news_list:
  #   data = {}
  #   data['Lenta.ru'] = item
  #   db.news.insert_one(data)
  #
  # for item in news_time:
  #   data = {}
  #   data['time'] = item
  #   db.news.insert_one(data)
  #
  # for item in news_link:
  #   data = {}
  #   data['link'] = url + item
  #   db.news.insert_one(data)

  # db.news.insert_one(
  #   {
  #     'Lenta.ru': news_list,
  #     'time': news_time,
  #     'link': url + news_link
  #   }
  # )
  for document in db.news.find():
    print(document)

if __name__ == '__main__':
    parsing()

