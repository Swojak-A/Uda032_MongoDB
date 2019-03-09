#!/usr/bin/env python
"""
aggregation framework pipeline

collection -> stage 1 ... stage n -> result
"""

# $group - groups certain values
# $sort - sorts basing on certain value
# $skip - skip certain number of documents from the begining
# $limit - limits to certain number of documents


from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def single_result():
    result = db.twitter.find_one()

    return result

def most_tweets():
    result = db.twitter.aggregate([
        {"$group" : {"_id" : "$user.screen_name", "count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1},},
        {"$skip" : 1},
        {"$limit" : 5}
    ])

    return result


if __name__ == '__main__':
    # single_result = single_result()
    # print("Single result:")
    # pprint(single_result)
    # print("")

    aggregated_result = most_tweets()
    print("Aggregated result:")
    pprint(list(aggregated_result))

