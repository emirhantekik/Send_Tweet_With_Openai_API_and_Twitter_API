import tweepy

# API Key ve API Key Secret değişkene atayın
consumer_key = "Twitter_API_key"
consumer_secret = "Twitter_API_secret_key"
access_token = "your_acccess_token"
access_token_secret = "your_access_secret"

# Yetkilendirme yap
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API objesini oluştur
api = tweepy.API(auth)

# user_timeline fonksiyonunu kullanarak kendi hesabınızda attığınız son 2 twiti okuyun
tweets = api.user_timeline(count=2)
for tweet in tweets:
    print(tweet.text)

hashtag = "search"
tweets = api.search_tweets(q=hashtag, count=10)

for tweet in tweets:
    if tweet is None:
        print("Not Found")
    else:
        print()
        print("Who is send tweet ? " + tweet.user.screen_name)
        tweet_link = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}"
        print(hashtag +" search result" + ":" + tweet.text)
        print(tweet.user.name +" "+ tweet.user.id_str)
        print(tweet_link)

# Elde ettiğiniz twitin linkine ihtiyacınız olursa print(tweet_link) eklemeniz yeterli
tweet_link = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}"

# What is the text in tweet?
# tweet = "Hello, Twitter! This tweet is from Python!🐍 #Python #Tweepy"

# if(api.update_status(tweet)):
#     print("True")

import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question(prompt):
    completions = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()

    return message

question = "What is the capital of Turkey?"
result = ask_question(question)

print(f"Q: {question}\nA: {result}")