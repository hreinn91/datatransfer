import psycopg2

# mock
# aggr_mongo
# pg_migration

def create_table(cursor):
    create_table_with_index = ('''CREATE TABLE task_count
            (id INT PRIMARY KEY       NOT NULL,
            unit            INT       NOT NULL,
            datetime        timestamp NOT NULL,
            count           INT       NOT NULL);''',
                               '''CREATE INDEX ON task_count(unit);''',
                               '''CREATE INDEX ON task_count(datetime);''')
    for command in create_table_with_index:
        cursor.execute(command)
    return


# Note User and Password are mocked
def create_task_count_pg_table(psql_db_name):
    try:

        # Connect to PostgreSQL
        connection = psycopg2.connect(user='test_user',
                                      password='password',
                                      host='/tmp/',
                                      database=psql_db_name)

        cursor = connection.cursor()
        cursor.execute('SELECT version();')
        record = cursor.fetchone()
        print('You are connected to - ', record, '\n')
        create_table(cursor)
        connection.commit()

    except(Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print('PostgreSQL connection closed')
    return
