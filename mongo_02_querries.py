from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def find(db):

    # range queries - $gt, $lt, $gte, $lte, $ne
    # query = {"dimensions.weight" : {"$gte" : 750, "$lte": 1000}}
    # you can also use a datetime or a string - this will result with an IndexError in this query tho
    # query = {"foundingDate": {"$gt": datetime(2000, 12, 31, 1, 1)}}

    # $exists operator
    # query = {"bodyStyle" : {"$exists" : 1}}

    # $regex operator
    # query = {"manufacturer" : {"$regex" : ".*(Motors)"}}

    # using scalars
    # query = {"productionYears": 1980}
    # $in operator - returns an objects that have ANY of specific value
    # query = {"productionYears" : {"$in" : [1983, 2006]}}
    # $all operator - returns an objects that have ALL of specific value
    # query = {"productionYears" : {"$all" : [1983, 2006]}}

    # multiple data
    query = {"manufacturer" : {"$ne" : "Toyota"}, "productionYears" : {"$in" : [1988, 1989]}}

    results = db.autos.find(query)
    return results

def publish_results(results):
    n_autos = 0
    for e in results:
        pprint(e)
        n_autos += 1

    print("We found {} cars in db matching the criteria.".format(n_autos))



if __name__ == "__main__":
    main_query = find(db=db)
    publish_results(main_query)