import asyncio
import json
from twscrape import API
import time

async def main():
    start_time = time.time() 
    api = API()
    keywords='prabowo'
    query: str = f"""{keywords}(source:twitter_web_client
            OR source:twitter_web_app
            OR source:twitter_for_iphone
            OR source:twitter_for_ipad
            OR source:twitter_for_mac
            OR source:twitter_for_android
            OR source:tweetdeck
            OR source:tweetdeck_web_app)
            lang:id"""
    print(query)
    tweets = []
    async for tweet in api.search(query,limit=1, kv={"product": "Latest"}):
        tweets.append(tweet.json())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total waktu yang diperlukan: {elapsed_time} detik jumlah len {len(tweets)}")
    # Write tweets to JSON file
    with open("tweets1.json", "w") as json_file:
        json.dump(tweets, json_file, indent=4)
    
if __name__ == "__main__":
    asyncio.run(main())