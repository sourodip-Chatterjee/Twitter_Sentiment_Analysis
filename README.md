# Twitter Sentiment Analysis

This project uses the Twitter API and TextBlob for sentiment analysis on tweets related to a specific topic. It fetches recent tweets based on a keyword or hashtag and analyzes whether the sentiment is positive, negative, or neutral.

## Prerequisites

Before running the script, you need to have:
- A **Twitter Developer** account to access the Twitter API and get your API keys.
- Python installed on your machine.
- `tweepy` and `textblob` Python libraries.

## Setup

### 1. Install Dependencies

You need to install the required libraries. Run the following command:

```bash
pip install tweepy textblob
```

### 2. Get Twitter API Keys

To access Twitter's data, you'll need to generate API keys. Follow these steps:
1. Create a Twitter Developer account at [Twitter Developer](https://developer.twitter.com/).
2. Set up an application within your developer account and generate the following keys:
   - Consumer Key
   - Consumer Secret Key
   - Access Token
   - Access Token Secret

### 3. Update API Keys in the Script

In the Python script (`twitter_sentiment_analysis.py`), replace the following placeholders with your API keys:

```python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
```

## Usage

1. Run the script by providing a query (keyword or hashtag) for which you want to analyze sentiment:

```bash
python twitter_sentiment_analysis.py
```

2. The script will fetch the latest tweets related to the query and display the tweet along with its sentiment (Positive, Negative, or Neutral).

## Example Output

```plaintext
Tweet: Python is amazing for data science!
Sentiment: Positive

Tweet: I hate when my code doesn't work.
Sentiment: Negative
```

## How It Works

1. **Fetch Tweets**: The script uses the Tweepy library to interact with the Twitter API and fetch tweets based on the provided query.
2. **Sentiment Analysis**: The `TextBlob` library is used to analyze the sentiment of each tweet. TextBlob computes polarity, and based on the polarity value:
   - Positive if polarity > 0
   - Negative if polarity < 0
   - Neutral if polarity == 0
