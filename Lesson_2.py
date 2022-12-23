print(('*' * 25), 'Задание №1 к лекции № 2', ('*' * 25))
import requests
from lxml import html
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


