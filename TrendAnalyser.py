import pandas as pd
from textblob import TextBlob

# 🔹 Sample mock data (in reality you'd load a CSV or scrape tweets)
data = {
    'username': ['@tech_guy', '@ai_queen', '@meme_lord'],
    'tweet': [
        'I love how AI is changing the world! 🤖❤',
        'Honestly, social media is getting too toxic these days.',
        'Data Science memes are 🔥🔥🔥'
    ]
}

df = pd.DataFrame(data)

# 🔍 Analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

df['sentiment_score'] = df['tweet'].apply(get_sentiment)

# 🧠 Label it
df['sentiment'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')

# 📊 Show the vibes
print(df)