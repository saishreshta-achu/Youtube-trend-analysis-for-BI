import pandas as pd

class DataAnalyzer:
    def __init__(self, input_path):
        self.input_path = input_path

    def calculate_metrics(self):
        df = pd.read_csv(self.input_path)
        df["engagement_rate"] = (df["likes"] + df["comments"]) / df["views"]
        return df

    def top_categories(self, df):
        return df.groupby("category")["views"].sum().sort_values(ascending=False)

    def frequent_upload_times(self, df):
        df["hour"] = df["publish_date"].dt.hour
        return df["hour"].value_counts()

if __name__ == "__main__":
    analyzer = DataAnalyzer("../data/cleaned/cleaned_videos.csv")
    data = analyzer.calculate_metrics()
    print("Top Categories:")
    print(analyzer.top_categories(data))
    print("Frequent Upload Times:")
    print(analyzer.frequent_upload_times(data))