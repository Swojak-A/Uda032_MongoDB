#!/usr/bin/env python

# $match - find documents matching certain patter
# $project - takes requested field and passes them on; can be renamed, can be computed



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
        {"$match" : {"user.followers_count" : {"$gt" : 0},
                    "user.friends_count" : {"$gt" : 0}}},
        {"$project" : {"ratio" : {"$divide" : ["$user.followers_count",
                                               "$user.friends_count"]},
                       "screen_name" : "$user.screen_name"}},
        {"$sort" : {"ratio" : -1}},
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