import lineTool
import os
import requests
from datetime import datetime, timedelta, timezone, date


class YoutubeSpider():
    def __init__(self, api_key):
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.api_key = api_key

    def search_videos(self, query, published_after):
        """使用關鍵字搜尋影片"""
        path = f"search?part=snippet&maxResults=50&q={query}&type=video&videoDefinition=high&publishedAfter={published_after}&key={self.api_key}"
        data = self.get_html_to_json(path)
        return data

    def search_channel(self, channel_id):
        path = f"channels?part=statistics&id={channel_id}&key={self.api_key}"
        data = self.get_html_to_json(path)
        return data

    def get_html_to_json(self, path):
        """組合 URL 後 GET 網頁並轉換成 JSON"""
        api_url = f"{self.base_url}{path}"
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok:
            data = r.json()
        else:
            data = None
        return data


now = datetime.utcnow().replace(tzinfo=timezone.utc)
past_hour = timedelta(hours=1)
published_after = (now - past_hour).strftime("%Y-%m-%dT%H:%M:%SZ")

# 初始化爬蟲物件並搜尋符合條件的影片
spider = YoutubeSpider("AIzaSyAJFruuvplYGxgAQfaeRngmh2TelGcFF9w")
query = "出包"
data = spider.search_videos(query, published_after)
car_accident_list = []
# 輸出所有影片的標題

for item in data["items"]:
    #     lineTool.lineNotify(os.getenv('token'),item)
    dic = {}
    dic["title"] = item["snippet"]["title"]
    video_url_id = item["id"]["videoId"]
    dic["video_url"] = f"https://www.youtube.com/watch?v={video_url_id}"
    dic["author"] = item["snippet"]["channelTitle"]
    channel_id = item["snippet"]["channelId"]
    channel_data = spider.search_channel(channel_id)
    car_accident_list.append(dic)


car_massege = f"出包{car_accident_list}"

lineTool.lineNotify(
    "UcvSIOXpRcanKdXbf45xNHvDZ1CnSwkL0ANqBv2zBiA", "123")
