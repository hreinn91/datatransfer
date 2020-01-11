from pymongo import MongoClient


def create_task_count(mongo_db_name):
    original_collection = 'Task'
    new_collection = 'TaskCount'

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

    sort = {"$sort": {"_id": -1}}

    pipeline = [group]

    aggregate = col.aggregate(pipeline)
    aggr_col.insert_many(aggregate)
    aggr_col.create_index(unit_key)
    aggr_col.create_index(time_key)

    return
