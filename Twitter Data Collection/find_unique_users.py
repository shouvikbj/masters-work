from enum import unique
from itertools import count
import os
import json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

with open(f"{APP_ROOT}/tweets.json", "r") as json_file:
  data = json.load(json_file)

total_data_count = len(data)
count = 0

unique_users = {}
number_of_unique_users = 0

print("Finding unique users from available data..")
for tweet in data:
  print("{:.0f}% done".format((count/total_data_count)*100), end="\r")
  count += 1
  if tweet['user'] in unique_users.keys():
    unique_users[tweet['user']] += 1
  else:
    unique_users.update({tweet['user']: 1})
    number_of_unique_users += 1

print("{:.0f}% done".format(((count-1)/total_data_count)*100))

print(f"{number_of_unique_users} unique users found..")

print("Storing unique users' information..")

with open(f"{APP_ROOT}/unique_users.json", "w") as json_file:
  json_file.seek(0)
  json.dump(unique_users, json_file, indent=2)
