import psycopg2


def insert_data(data):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="BlaBla123",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO data (total_data) VALUES (%s)"""
        record_to_insert = (data,)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into data table", error)
