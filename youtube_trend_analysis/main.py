from src.data_collection import YouTubeDataCollector
from src.data_cleaning import DataCleaner
from src.analysis import DataAnalyzer
# from src.visualization import DataVisualizer
# from src.sentiment_analysis import SentimentAnalyzer
# from src.dashboard import Dashboard

def main():
    print("YouTube Trend Analysis CLI")
    print("1. Collect Data")
    print("2. Clean Data")
    print("3. Run Analysis")
    print("4. Visualize Results")
    print("5. Launch Dashboard")

    choice = input("Enter your choice: ")

    if choice == "1":
        API_KEY = "YOUR_API_KEY"
        collector = YouTubeDataCollector(API_KEY)
        trending_data = collector.fetch_trending_videos()
        if trending_data:
            collector.save_to_csv(trending_data, "data/raw/trending_videos.csv", "US")
    elif choice == "2":
        cleaner = DataCleaner("data/raw/trending_videos.csv", "data/cleaned/cleaned_videos.csv")
        cleaner.clean_data()
    elif choice == "3":
        analyzer = DataAnalyzer("data/cleaned/cleaned_videos.csv")
        data = analyzer.calculate_metrics()
        print("Top Categories:")
        print(analyzer.top_categories(data))
        print("Frequent Upload Times:")
        print(analyzer.frequent_upload_times(data))
    elif choice == "4":
        print("Visualization module not implemented yet.")
    elif choice == "5":
        print("Dashboard module not implemented yet.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()