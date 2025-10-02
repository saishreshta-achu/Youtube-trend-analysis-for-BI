import os
import requests
import pandas as pd

class YouTubeDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def fetch_trending_videos(self, region_code="US", max_results=50):
        url = f"{self.base_url}/videos"
        params = {
            "part": "snippet,statistics",
            "chart": "mostPopular",
            "regionCode": region_code,
            "maxResults": max_results,
            "key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def save_to_csv(self, data, output_path, region_code):
        videos = []
        for item in data.get("items", []):
            snippet = item.get("snippet", {})
            stats = item.get("statistics", {})
            videos.append({
                "title": snippet.get("title"),
                "channel": snippet.get("channelTitle"),
                "views": stats.get("viewCount"),
                "likes": stats.get("likeCount"),
                "comments": stats.get("commentCount"),
                "tags": snippet.get("tags"),
                "publish_date": snippet.get("publishedAt"),
                "category": snippet.get("categoryId"),
                "region": region_code
            })
        df = pd.DataFrame(videos)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    collector = YouTubeDataCollector(API_KEY)
    trending_data = collector.fetch_trending_videos()
    if trending_data:
        collector.save_to_csv(trending_data, "../data/raw/trending_videos.csv", "US")