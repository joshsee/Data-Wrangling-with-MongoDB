import json

def insert_data(data, db):

    # Your code here. Insert the data into a collection 'arachnid'
    bulk_data = []
    for row in data:
        bulk_data.append(row)

    db.arachnid.insert(bulk_data)


if __name__ == "__main__":

    # from pymongo import MongoClient
    # client = MongoClient("mongodb://localhost:27017")
    # db = client.examples
    db = None

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()