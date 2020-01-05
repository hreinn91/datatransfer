from pymongo import MongoClient
import pprint

test_db_name = 'testdb'
collection_name = 'Task'

id_key = 'taskId'
unit_key = 'unit'
time_key = 'datetime'

numb_mocked_docs = 1000

client = MongoClient()
db = client[test_db_name]
col = db[collection_name]

group = {
    "$group": {
        "_id": {
            "y": {"$year": "$" + time_key},
            "m": {"$month": "$" + time_key},
            "d": {"$dayOfMonth": "$" + time_key},
            "h": {"$hour": "$" + time_key},
            "unit": "$" + unit_key
        },
        "count": {"$sum": 1}
    }
}

sort = {"$sort": {"_id": -1}
        }

pipeline = [group, sort]

aggregate = col.aggregate(pipeline)

for doc in aggregate:
    pprint.pprint(doc)

print('done')
