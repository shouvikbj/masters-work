import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
import os

query = "(Religious hate OR political hate OR gender bias OR hate speech OR caste hate)"
tweets = []
limit = int(input("How many Tweets do you want to collect: "))
count = 0

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

print(f"Collecting {limit} Tweets..")
single_tweet = ""
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(type(vars(tweet)))
    # break
    if len(tweets) == limit:
        single_tweet = tweet
        print("{:.0f}% done".format((count/limit)*100))
        break
    else:
        print("{:.0f}% done".format((count/limit)*100), end="\r")
        count += 1
        a_tweet = vars(tweet)
        for key, value in a_tweet.items():
            # print(key, type(value))
            if ((type(value) != dict) or (type(value) != list)):
                a_tweet[key] = str(value)
        tweets.append(a_tweet)

print("Storing Tweets..")

with open(f"{APP_ROOT}/tweets.json", "w") as json_file:
    json_file.seek(0)
    json.dump(tweets, json_file, indent=2)

with open(f"{APP_ROOT}/tweets.json", "r") as json_file:
    data = json.load(json_file)
    print(f"{len(data)} Tweets stored..")

df = pd.DataFrame(tweets, columns=[key for key,_ in vars(tweet).items()])
# print(df)
df.to_csv("tweets.csv", index=False)