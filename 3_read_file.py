#!/bin/python
import csv 
import psycopg2

dict_list = []

with open ("vm_state_copy.out", 'r') as file:
    for row in file:
        line = row.strip()
        values = line.split(',')
        drop_stat_dict = {
             'chunk_stat': values[5]
        }
        dict_list.append(drop_stat_dict)

        
try:
    connection = psycopg2.connect(
        database="python_test",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()
       
        
    check_drop_chunk = 'select datname, usename, pid, query, query_start from pg_stat_activity;'
        

    if 'dropped' in dict_list['chunk_stat'].lower():
        print("Chunks already dropped")
    else:
        print("Drop Chunk Process will be initiated")
        
        query = sql.SQL("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.usename != {}").format(sql.Literal('postgres'))
        cursor.execute(query)
        connection.commit()

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    connection.close()



