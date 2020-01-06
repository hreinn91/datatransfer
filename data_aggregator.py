from pymongo import MongoClient
import pprint
import psycopg2
import sql

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

    return


def create_task_count_pg_table(cursor):
    create_table_with_index = ('''CREATE TABLE task_count
            (id INT PRIMARY KEY       NOT NULL,
            unit            INT       NOT NULL,
            datetime        timestamp NOT NULL,
            count           INT       NOT NULL);''',
                               '''CREATE INDEX ON task_count(unit);''')
    for command in create_table_with_index:
        cursor.execute(command)
    return


# Note User and Password are mocked
def data_aggregation_to_pg(mongo_db_name, new_collection, psql_db_name):
    # test_db
    # test_user
    # password

    try:

        # Connect to PostgreSQL
        connection = psycopg2.connect(user='test_user',
                                      password='password',
                                      host='/tmp/',
                                      database=psql_db_name)

        cursor = connection.cursor()
        # print(connection.get_dns_parameters(), '\n')
        cursor.execute('SELECT version();')
        record = cursor.fetchone()
        print('You are connected to - ', record, '\n')

        # Connect to MongoDB
        client = MongoClient()
        db = client[mongo_db_name]
        aggr_col = db[new_collection]

        create_task_count_pg_table(cursor)

        for doc in aggr_col.find():
            pprint.pprint(doc)

        connection.commit()

    except(Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print('PostgreSQL connection closed')

    return


print('done')
