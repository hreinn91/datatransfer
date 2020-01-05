from pymongo import MongoClient

test_db_name = 'testdb'
client = MongoClient()
db = client['test-database']

