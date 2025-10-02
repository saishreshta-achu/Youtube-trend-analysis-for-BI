import pandas as pd
import os

class DataCleaner:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def clean_data(self):
        df = pd.read_csv(self.input_path)
        df.drop_duplicates(inplace=True)
        df.fillna("Unknown", inplace=True)
        df["publish_date"] = pd.to_datetime(df["publish_date"], errors="coerce")
        df["views"] = pd.to_numeric(df["views"], errors="coerce")
        df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
        df["comments"] = pd.to_numeric(df["comments"], errors="coerce")
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        df.to_csv(self.output_path, index=False)

if __name__ == "__main__":
    cleaner = DataCleaner("../data/raw/trending_videos.csv", "../data/cleaned/cleaned_videos.csv")
    cleaner.clean_data()