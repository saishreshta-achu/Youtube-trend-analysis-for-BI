# File: youtube_trend_analysis/src/insights.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your YouTube data (example CSV)
df = pd.read_csv('youtube_data.csv')

# Example columns: ['video_title', 'views', 'likes', 'comments', 'watch_time_minutes', 'upload_date']

# Convert upload_date to datetime
df['upload_date'] = pd.to_datetime(df['upload_date'])

# Top 10 videos by watch time
top_watchtime = df.nlargest(10, 'watch_time_minutes')

# Plot top 10 videos by watch time
plt.figure(figsize=(12,6))
sns.barplot(x='watch_time_minutes', y='video_title', data=top_watchtime, palette='viridis')
plt.title('Top 10 Videos by Watch Time')
plt.xlabel('Watch Time (Minutes)')
plt.ylabel('Video Title')
plt.tight_layout()
plt.savefig('../screenshots/top_watchtime.png')
plt.show()

# Monthly watch time trend
df['month'] = df['upload_date'].dt.to_period('M')
monthly_watchtime = df.groupby('month')['watch_time_minutes'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(x='month', y='watch_time_minutes', data=monthly_watchtime, marker='o', color='blue')
plt.title('Monthly Watch Time Trend')
plt.xlabel('Month')
plt.ylabel('Total Watch Time (Minutes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../screenshots/monthly_watchtime.png')
plt.show()

# Engagement ratio: likes per view
df['engagement_ratio'] = df['likes'] / df['views']

# Top 10 engaging videos
top_engagement = df.nlargest(10, 'engagement_ratio')

plt.figure(figsize=(12,6))
sns.barplot(x='engagement_ratio', y='video_title', data=top_engagement, palette='coolwarm')
plt.title('Top 10 Videos by Engagement Ratio (Likes/Views)')
plt.xlabel('Engagement Ratio')
plt.ylabel('Video Title')
plt.tight_layout()
plt.savefig('../screenshots/top_engagement.png')
plt.show()
