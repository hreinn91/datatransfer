from pymongo import MongoClient
import datetime

def hello():
    print('Hellooooooooooooooooo')

def mock_data(database_name, numb_docs):
    collection_name = 'Task'

    id_key = 'taskId'
    unit_key = 'unit'
    time_key = 'datetime'

    client = MongoClient()
    db = client[database_name]
    col = db[collection_name]

    mock_list = []

    for i in range(numb_docs):
        mock_list.append(
            dict([
                (id_key, i),
                (unit_key, i % 5 + 1),
                (time_key, datetime.datetime.utcnow() - datetime.timedelta(minutes=i * 2))
            ]))

    col.insert_many(mock_list)
    col.create_index(unit_key)
    col.create_index(time_key)
    return
