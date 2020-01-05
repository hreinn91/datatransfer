from pymongo import MongoClient
import datetime
import pprint
from bson.son import SON

test_db_name = 'testdb'
collection_name = 'Task'

id_key = 'taskId'
unit_key = 'unit'
time_key = 'datetime'

numb_mocked_docs = 1000

client = MongoClient()
db = client[test_db_name]
col = db[collection_name]

proj = {"$project": {
    "y": {"$year": "$" + time_key},
    "m": {"$month": "$" + time_key},
    "d": {"$dayOfMonth": "$" + time_key},
    "h": {"$hour": "$" + time_key},
    "u": "$" + unit_key}
}

group = {"$group": {
    "_id": {"year": "$y", "month": "$m", "day": "$d", "hour": "$h", unit_key: "$u"},
    "count": {"$sum": 1}}
}

sort = {"$sort":
            {"_id": -1}
        }

group2 = {
    "$group": {
        "_id": {
            "y": {"$year": "$"+time_key},
            "m": {"$month": "$"+time_key},
            "d": {"$dayOfMonth": "$"+time_key},
            "h": {"$hour": "$"+time_key},
            "u": "$"+unit_key
        },
        "count": {"$sum": 1}
    }
}

# pipeline = [proj, group, sort]
pipeline = [group2, sort]

aggregate = col.aggregate(pipeline)

for doc in aggregate:
    pprint.pprint(doc)

print('done')
