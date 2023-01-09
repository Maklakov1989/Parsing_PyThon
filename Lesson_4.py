import requests
from lxml import html
from pymongo import MongoClient
import pprint

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
  params = {
    'message': "",
  }
  url = 'https://lenta.ru/'
  link = requests.get(url, headers=headers, params=params)
  news = html.fromstring(link.text)
  #news_list = news.xpath("//span[contains(@class,'card-mini__title')]/text()")[0: 15]
  #news_time = news.xpath("//div[contains(@class,'card-mini__info')]/time/text()")[0: 15]
  #news_link = news.xpath("//a[contains(@class, 'card-mini')]/@href")[0: 15]
  for i in news:
    x = 1
    db.news.insert_one(
      {
        'Lenta.ru' : news.xpath("//span[contains(@class,'card-mini__title')]/text()")[x],
        'time' : news.xpath("//div[contains(@class,'card-mini__info')]/time/text()")[x],
        'link' : news.xpath("//a[contains(@class, 'card-mini')]/@href")[x]
      }
    )
    x = x + 1
  for document in db.news.find():
    print(document)


parsing()