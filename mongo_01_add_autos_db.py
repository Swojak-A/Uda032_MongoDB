#!/usr/bin/env python
"""
Udacity instructions:

Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""

from autos import process_file

def insert_autos(infile, db):
    data = process_file(infile)
    db.autos.insert(data)


if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    # uncomment to insert data
    # insert_autos('autos-small.csv', db)

    # uncomment to check for data
    query = db.autos.find({"manufacturer" : "Mazda"})
    for e in query:
        pprint(e)

