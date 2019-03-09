#!/usr/bin/env python

# $unwind - takes an array from document and ouputs it as element


from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def single_result():
    result = db.twitter.find_one()

    return result

def ff_ratio():
    """ return an object showing fallowers to friends ratio """
    result = db.twitter.aggregate([
        {"$unwind" : "$entities.user_mentions"},
        {"$group" : {"_id" : "$user.screen_name",
                     "count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1}},
        {"$limit" : 3}
    ])

    return result


if __name__ == '__main__':
    # single_result = single_result()
    # print("Single result:")
    # pprint(single_result)
    # print("")

    aggregated_result = ff_ratio()
    print("Aggregated result:")
    pprint(list(aggregated_result))