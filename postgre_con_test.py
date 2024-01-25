import psycopg2

db_host = "localhost"
db_port = "5432"
db_name = "python_test"
db_user = "test"
db_password = "test"

try:
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
