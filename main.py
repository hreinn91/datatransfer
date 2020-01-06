
from data_aggregator import data_aggregation

mongo_db_name = 'testdb'
original_collection_name = 'Task'
new_collection_name = 'TaskCount'

data_aggregation(mongo_db_name, original_collection_name, new_collection_name)


