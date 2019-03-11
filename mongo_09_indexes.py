#!/usr/bin/env python

"""
indexes are the way we can intentionally structure our data in db to provide faster querries.
it is adviced to create indexes for the querries that are expected to be most frequent
why not all querries? well, indexes takes some space and updating them when inserting data into db takes time. they are simply not costless.

in shell:
db.ensureIndex({"name":1})
in pymongo:
ensure_index()

full lesson:
https://classroom.udacity.com/courses/ud032/lessons/760758686/concepts/7842387540923

geospatial indexes:
location : [x, y]
ensureIndex({"location": ... }) - command to build an index in shell
ensure_index("example_key", pymongo.GEO2D) - a method from pymongo
$near - operator to run query based on geospatial index
"""