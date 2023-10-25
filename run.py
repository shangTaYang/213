import feedparser
from datetime import datetime, timedelta, timezone,date
# RSS feed的URL
def search_no():
    rss_url = "https://trends.google.com.tw/trends/trendingsearches/daily/rss?geo=TW"
    
    # 使用feedparser库来解析RSS数据
    feed = feedparser.parse(rss_url)
    
    # 遍历并提取每个条目的标题和链接
    now = datetime.now(
        tz=timezone(timedelta(hours=8)))
    now_all = now.strftime('%Y/%m/%d ')
    print(now_all+"熱搜排行")
    for index, entry in enumerate(feed.entries):
      if index <5:
        # print(f'第{index+1}名:{entry.title}\n相關新聞:{entry.ht_news_item_title}',end='\n\n')
        lineTool.lineNotify(os.getenv('token'), f'第{index+1}名:{entry.title}\n相關新聞:{entry.ht_news_item_title}',end='\n\n')
