from data_aggregator import data_aggregation_to_pg
import sys



def main():
    if len(sys.argv) < 2:
        print("Error required database input arg")
        return
    elif len(sys.argv) > 2:
        print("Error too many input args. Requires database input arg")
        return


    greeting = sys.argv[1]
    print(greeting)

    mongo_db_name = 'testdb'
    pg_db_name = 'test_db'

    original_collection_name = 'Task'
    new_collection_name = 'TaskCount'

    # data_aggregation(mongo_db_name, original_collection_name, new_collection_name)
    #data_aggregation_to_pg(mongo_db_name, new_collection_name, pg_db_name)



if __name__ == "__main__":
    main()



