import sys
from data_mock import hello

def main():
    if len(sys.argv) < 2:
        print("Error no specified operations")
        return

    mongo_db_name = 'testdb'
    pg_db_name = 'test_db'
    operations = sys.argv
    mock_data_count = 10000

    if 'mock_data' in operations:
        hello()

    return


if __name__ == "__main__":
    main()
