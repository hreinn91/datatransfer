from pymongo import MongoClient
import datetime


test_db_name = 'testdb'
collection_name = 'Task'

id_key = 'taskId'
unit_key = 'unit'
time_key = 'datetime'

numb_mocked_docs = 170

client = MongoClient()
db = client[test_db_name]
col = db[collection_name]

mock_list = []

for i in range(numb_mocked_docs):
    mock_list.append(
        dict([
            (id_key, i),
            (unit_key, i%5 + 1),
            (time_key, datetime.datetime.utcnow() - datetime.timedelta(minutes=i*2))
        ]))

col.insert_many(mock_list)

