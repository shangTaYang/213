import lineTool
import os
import requests
from datetime import datetime, timedelta, timezone,date
import re
import feedparser
from bs4 import BeautifulSoup




def google_news():
    now = datetime.now(
        tz=timezone(timedelta(hours=8)))
    now_all = now.strftime('%Y/%m/%d ')
    headers = {
        'user-agent':
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.62',
    }

    # 發出網路請求 GET
    resp = requests.get(
        'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant',
        headers=headers)

    # 使用 BeautifulSoup 解析內容為 BeautifulSoup 物件
    soup = BeautifulSoup(resp.text, "html.parser")
    # 解析抓取 class name 為 NiLAwe 區塊（每一個新聞組合）
    rows = soup.select("c-wiz div c-wiz h4")
    asd = "\n\n"
    news = [now_all + " 重點新聞" + asd]
    for i in rows:
        aaa = i.text
        ddd = " "
        news.append(aaa + ddd + asd)
    del news[11:]
    
    lineTool.lineNotify(os.getenv('token'), news)
       
def get_ettoday_social_news_url(url):
  headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
  }
  resp = requests.get(url, headers=headers)
  soup = BeautifulSoup(resp.text, "html.parser")
  rows = soup.select(".part_list_2 h3")
  news = []
  for i in rows:
    if i.select('a i'):
      title = i.select("a")[0].text
      news_url = i.find("a").get("href")
      data = {}
      data["title"] = title
      data["news_url"] = f'{ettday}{news_url}'
      news.append(data)
    else:
      continue
  return news

def china_news_job():
  china_news = get_ettoday_social_news_url(f'{ettday}/news-list-{today}-3.htm')
  del china_news[2:] 
  # china_news是字串包字典 [{title:123,url:123},....]
  for i in china_news:  # 取出每個字典 i = {title:123,url:123}
    title = i["title"]
    url = i["news_url"]
    if re.search(chubao, title):
        sbb = title + url 
        lineTool.lineNotify(os.getenv('token'), sbb)

def social_news_job():
  social_news = get_ettoday_social_news_url(
    f'{ettday}/news-list-{today}-6.htm')
  del social_news[2:]
  # china_news是字串包字典 [{title:123,url:123},....]
  for i in social_news:  # 取出每個字典 i = {title:123,url:123}
    title = i["title"]
    url = i["news_url"]
    if re.search(chubao, title):
        sbb = title + url 
        lineTool.lineNotify(os.getenv('token'), sbb)

def Local_news_job():
  Local_news = get_ettoday_social_news_url(f'{ettday}/news-list-{today}-7.htm')
  del Local_news[2:]
  # china_news是字串包字典 [{title:123,url:123},....]
  for i in Local_news:  # 取出每個字典 i = {title:123,url:123}
    title = i["title"]
    url = i["news_url"]
    if re.search(chubao, title):
        sbb = title + url 
        lineTool.lineNotify(os.getenv('token'), sbb)

def International_news_job():
  International_news = get_ettoday_social_news_url(
    f'{ettday}/news-list-{today}-2.htm')
  del International_news[2:]
  # china_news是字串包字典 [{title:123,url:123},....]
  for i in International_news:  # 取出每個字典 i = {title:123,url:123}
    title = i["title"]
    url = i["news_url"]
    if re.search(chubao, title):
        sbb = title + url 
        lineTool.lineNotify(os.getenv('token'), sbb)

chubao = r'''((出包)|(糗)|(笑死)|(丟臉)|(尷尬)|(錯誤)|(出糗)|(失誤)|'''

  
today = date.today()
ettday = "https://www.ettoday.net/news"
china_news = f'{ettday}/news-list-{today}-3.htm'
social_news = f'{ettday}/news-list-{today}-6.htm'
Local_news = f'{ettday}/news-list-{today}-7.htm'
International_news = f'{ettday}/news-list-{today}-2.htm'
  


if (datetime.utcnow() + timedelta(hours=8)).strftime("%H") in "01" :
    china_news_job()
    social_news_job()
    Local_news_job()
    International_news_job()
