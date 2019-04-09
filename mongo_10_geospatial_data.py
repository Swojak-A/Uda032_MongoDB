#!/usr/bin/env python

# $push - adds an element to an array
# $addToSet - adds an element to a set

from pymongo import MongoClient, GEO2D
from bson.son import SON

import os
import json
from pprint import pprint


client = MongoClient("mongodb://localhost:27017")
db = client.examples

""" import to db """

def construct_geojson(data):
    result_dict = {}

    result_dict["type"] = "Feature"
    result_dict["geometry"] = {
        "type" : "Point",
        "coordinates" : [data["longitude"], data["latitude"]]
    }
    result_dict["properties"] = {}

    result_dict["properties"]["id_name"] = data["identification"]
    result_dict["properties"]["common_name"] = data["common_name"]
    result_dict["properties"]["description"] = data["description"]
    result_dict["properties"]["id_name"] = data["identification"]
    result_dict["properties"]["categories"] = data["categories"]
    result_dict["properties"]["state"] = data["state"]
    result_dict["properties"]["register_number"] = data["register_number"]
    result_dict["properties"]["dating_of_obj"] = data["dating_of_obj"]
    result_dict["properties"]["location_details"] = {}
    result_dict["properties"]["location_details"]["place_id"] = data["place_id"]
    result_dict["properties"]["location_details"]["country_code"] = data["country_code"]
    result_dict["properties"]["location_details"]["place_name"] = data["place_name"]
    result_dict["properties"]["location_details"]["commune_name"] = data["commune_name"]
    result_dict["properties"]["location_details"]["district_name"] = data["district_name"]
    result_dict["properties"]["location_details"]["voivodeship_name"] = data["voivodeship_name"]

    return result_dict

def browse_files(path="files/zip/relics-json/", limit=10, place_query=None):
    results = []

    n = 1
    for file in os.listdir(path):
        print(n)
        print(path + file)

        with open(path + file, "r", encoding="UTF8") as fp:
            relic_dict = json.load(fp)

        if place_query != None:
            if "place_name" in relic_dict.keys() and "Warszawa" in relic_dict["place_name"]:
                pprint(relic_dict)
                result_dict = construct_geojson(relic_dict)

                results.append(result_dict)
                # json_path = "files/geojson/"
                # file_name = json_path + file
                # with open(file_name, "w", encoding="UTF8") as fp:
                #     json.dump(result_dict, fp)

        n += 1
        if n >= limit:
            break

""" db """

def ensure_index(db):
    db.relics.create_index([("geometry.coordinates", GEO2D)])

def find_near(db):
    # query = {"geometry.coordinates" : {"$near" : [20.98, 52.21]}}
    # query = {"geometry.coordinates": SON([("$near", [20.98, 52.21]), ("$maxDistance", 1)])}
    # query = {"geometry.coordinates" : {"$within": {"$box": [[20.989356, 52.221297], [20.975609, 52.217409]]}}}
    query = {"geometry.coordinates": {"$within": {"$polygon": [[20.989356, 52.221297], [20.975609, 52.217409], [20.978281, 52.223413]]}}}

    results = db.relics.find(query).limit(1)

    n = 0
    for doc in results:
        pprint(doc)
        n += 1

    print(n)
    print(results.count())


if __name__ == "__main__":
    # browse_files(limit=9000000, place_query="Warszawa")
    ensure_index(db=db)

    find_near(db=db)




