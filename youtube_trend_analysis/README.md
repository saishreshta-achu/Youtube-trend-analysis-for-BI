# YouTube Trend Analysis for Business Intelligence

This project analyzes YouTube trends using machine learning and Python libraries. It provides insights into trending videos, categories, and user engagement.

## Features

1. **Data Collection**: Fetch trending video data using the YouTube Data API.
2. **Data Cleaning**: Remove duplicates, handle missing values, and normalize data.
3. **Analysis**: Calculate engagement metrics, analyze categories, and identify frequent upload times.
4. **Visualization**: Generate plots for insights.
5. **Sentiment Analysis**: Perform sentiment analysis on video comments.
6. **Dashboard**: Interactive dashboard to display KPIs and visualizations.

## Folder Structure

```
youtube_trend_analysis/
├── data/               # store raw and cleaned datasets
├── notebooks/          # Jupyter notebooks for analysis
├── src/                # Python scripts
│   ├── __init__.py
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── sentiment_analysis.py
│   └── dashboard.py
├── requirements.txt    # dependencies
├── main.py             # main entry point
├── README.md
```

## Setup

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your YouTube Data API key in the appropriate script.

## Usage

Run the main script:
```bash
python main.py
```

Follow the CLI menu to perform various tasks like data collection, cleaning, analysis, and visualization.

## Dependencies

- google-api-python-client
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- streamlit
- textblob
- nltk
- wordcloud

## License

This project is licensed under the MIT License.