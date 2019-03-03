from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples


def update(db):
    query = {"manufacturer": {"$regex": ".*(Motors)"}}
    item = db.autos.find_one(query)

    # using assing
    # pprint(item)
    # item["testField"] = "test2"

    #using $set
    db.autos.update(query, {"$set" : { "productionYears" : [x for x in range(1963, 1980)] }})

    # here I make sure that none of the test values were actually input in the db
    # db.autos.update(query, {"$unset" : { "testField" : "" }})

    pprint(db.autos.find_one(query))


if __name__ == "__main__":
    update(db=db)