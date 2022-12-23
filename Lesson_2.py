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
  news_dict = {}
  for new in news:
    news_list = new.xpath("//span[contains(@class,'card-mini__title')]/text()")[0]
    news_time = new.xpath("//div[contains(@class,'card-mini__info')]/time/text()")[0]
    news_dict[news_list] = {
      'time' : news_time,
                            }
  print(news_dict)

parsing()


