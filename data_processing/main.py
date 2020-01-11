import sys
from data_mock import mock_data
from mongo_task_aggr import create_task_count
from pg_task_migration import create_task_count_pg_table
# mock
# aggr
# migration

def main():
    if len(sys.argv) < 2:
        print("Error no specified operations")
        return

    operations = sys.argv
    mongo_db_name = 'testdb'
    pg_db_name = 'test_db'
    mock_data_count = 10000

    if 'mock' in operations:
        print('mock')
        #mock_data(mongo_db_name, mock_data_count)

    if 'aggr' in operations:
        print('aggr')
        #create_task_count(mongo_db_name)

    if 'migration' in operations:
        print('migration')
        #create_task_count_pg_table(pg_db_name)

    return


if __name__ == "__main__":
    main()
