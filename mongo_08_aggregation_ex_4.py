#!/usr/bin/env python

# $push - adds an element to an array
# $addToSet - adds an element to a set


from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def single_result():
    result = db.twitter.find_one()

    return result

def most_unique_hashtags_by_users():
    # shows the top 30 users who used most unique hashtags
    # you can comment out certain stages to look how the query is changing
    result = db.twitter.aggregate([
        {"$match" : {"entities.hashtags" :
                         {"$exists" : 1,
                          "$gt" : []
                          , "$not" : {"$size" : 1}
                          }}},
        {"$project" : {"_id" : "$user.screen_name", "hashtags" : "$entities.hashtags.text"}},
        {"$unwind" : "$hashtags"},
        {"$project" : {"_id" : "$_id", "hashtags" : "$hashtags"}}, # this one is in only to show how to comment out a single stage
        {"$group" : {
            "_id" : "$_id",
            "unique_hashtags" : {"$addToSet" : "$hashtags"}
        }},
        {"$project" : {
            "_id" : "$_id",
            "count" : {"$size" : "$unique_hashtags"}
        }},
        {"$sort" : {"count" : -1}},
        {"$limit" : 30}
    ])

    return result


if __name__ == '__main__':
    # single_result = single_result()
    # print("Single result:")
    # pprint(single_result)
    # print("")

    aggregated_result = most_unique_hashtags_by_users()
    print("Aggregated result:")
    pprint(list(aggregated_result))