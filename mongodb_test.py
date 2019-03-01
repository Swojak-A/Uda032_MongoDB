def add_city(db):
    # Changes to this function will be reflected in the output.
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.cities.insert({"name": "Chicago"})


def get_city(db):
    return db.cities.find_one()


def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.examples
    return db


if __name__ == "__main__":
    # For local use
    db = get_db() # uncomment this line if you want to run this locally

    # uncomment to add data to db
    # add_city(db)

    # uncomment to retrieve data
    print(get_city(db))
