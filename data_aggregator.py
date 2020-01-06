from pymongo import MongoClient
import pprint

test_db_name = 'testdb'
collection_name = 'Task'


def data_aggregation(mongo_db_name, original_collection, new_collection):

    unit_key = 'unit'
    time_key = 'datetime'

    client = MongoClient()
    db = client[mongo_db_name]
    col = db[original_collection]
    aggr_col = db[new_collection]

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
    aggr_col.insert_many(aggregate)

    # for doc in aggregate:
    #     pprint.pprint(doc)

    return


print('done')
