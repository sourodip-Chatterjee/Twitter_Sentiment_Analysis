import tweepy
from textblob import TextBlob
import os
import logging

# Set up logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Authenticate to Twitter
def authenticate_twitter():
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_SECRET')

    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise ValueError("Twitter API keys are missing! Please set them in the environment variables.")

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        logging.info("Authentication successful.")
        return api
    except tweepy.TweepError as e:
        logging.error(f"Error during authentication: {e}", exc_info=True)
        raise

# Function to fetch tweets
def fetch_tweets(api, query, count=10):
    if not query.strip():
        logging.error("Query string is empty.")
        return None
    try:
        tweets = api.search_tweets(q=query, count=count, lang='en', tweet_mode='extended')
        return tweets
    except tweepy.TweepError as e:
        logging.error(f"Error fetching tweets: {e}", exc_info=True)
        return None

# Function to analyze sentiment
def analyze_sentiment(tweets):
    analyzed_data = []
    for tweet in tweets:
        try:
            text = tweet.full_text
            analysis = TextBlob(text)
            sentiment = (
                'Positive' if analysis.sentiment.polarity > 0 else 
                'Negative' if analysis.sentiment.polarity < 0 else 
                'Neutral'
            )
            analyzed_data.append({'tweet': text, 'sentiment': sentiment})
        except Exception as e:
            logging.error(f"Error analyzing sentiment for tweet: {tweet.full_text} - {e}", exc_info=True)
    return analyzed_data

# Main script
if __name__ == '__main__':
    setup_logging()
    try:
        api = authenticate_twitter()
        query = 'Python'  # Topic or hashtag you want to search tweets for
        tweets = fetch_tweets(api, query, count=10)
        if tweets:
            sentiment_results = analyze_sentiment(tweets)
            for result in sentiment_results:
                print(f"Tweet: {result['tweet']}\nSentiment: {result['sentiment']}\n")
        else:
            logging.info("No tweets fetched.")
    except Exception as e:
        logging.error(f"Critical error occurred: {e}", exc_info=True)
