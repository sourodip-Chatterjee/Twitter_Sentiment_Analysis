# Twitter Sentiment Analysis Tool

This repository provides a Python script for fetching and analyzing tweets based on a search query. It uses the Twitter API via Tweepy and performs sentiment analysis with TextBlob.

---

## Features

- **Fetch Tweets**: Retrieves tweets based on a specified search query.
- **Sentiment Analysis**: Classifies tweets as Positive, Negative, or Neutral.
- **Rate Limit Handling**: Automatically handles Twitter API rate limits.
- **Secure API Keys**: Uses environment variables to protect API credentials.
- **Logging**: Provides logs for tracking progress and debugging.

---

## Requirements

- Python 3.7+
- A valid Twitter Developer account and API credentials

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/twitter-sentiment-analysis.git
   cd twitter-sentiment-analysis
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root or set the following environment variables:
   ```env
   TWITTER_CONSUMER_KEY=your_consumer_key
   TWITTER_CONSUMER_SECRET=your_consumer_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_SECRET=your_access_secret
   ```

---

## Usage

1. **Run the Script**:
   ```bash
   python sentiment_analysis.py
   ```

2. **Modify the Search Query**:
   Update the `query` variable in the script to search for a specific topic or hashtag:
   ```python
   query = 'Python'  # Replace 'Python' with your topic
   ```

3. **View Results**:
   The script will print each tweet and its sentiment (Positive, Negative, or Neutral):
   ```
   Tweet: Python is amazing!
   Sentiment: Positive

   Tweet: I hate debugging Python code.
   Sentiment: Negative
   ```

---

## Project Structure

- `sentiment_analysis.py`: Main script for fetching tweets and performing sentiment analysis.
- `requirements.txt`: List of Python dependencies.

---

## Dependencies

- [Tweepy](https://www.tweepy.org/): Twitter API wrapper for Python.
- [TextBlob](https://textblob.readthedocs.io/): Simplified text processing for sentiment analysis.

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Notes

1. **Twitter API Access**:
   - Ensure your Twitter Developer account is set up to retrieve the required API keys.
   - Be aware of Twitter API rate limits when fetching tweets.

2. **Sentiment Analysis**:
   - TextBlob provides basic sentiment analysis. For better accuracy, consider using advanced libraries like VADER or transformers-based models.
