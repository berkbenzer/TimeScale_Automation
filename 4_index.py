
hypertable = [('conditions', '{"drop_after": "7 days", "hypertable_id": 1}'), ('conditions_1', '{"drop_after": "15 days", "hypertable_id": 3}'), ('conditions_2', '{"drop_after": "10 days", "hypertable_id": 4}')]




'''
hypertable = [
    ('conditions', '{"drop_after": "7 days", "hypertable_id": 1}'),
    ('conditions_1', '{"drop_after": "15 days", "hypertable_id": 3}'),
    ('conditions_2', '{"drop_after": "10 days", "hypertable_id": 4}')
]
'''

    
def get_drop_scripts():
    for table, params_json in hypertable:
        params_dict = eval(params_json)  
        interval_days = params_dict.get('drop_after')

        if interval_days:
            sql_statement = f"SELECT drop_chunks('{table}', INTERVAL '{interval_days}');"
            print(sql_statement)
            
            
            
def check_drop_chunk_statement():
    statement = []
    check_drop_statment= 'select  datname,pid,usename,query,query_start from pg_stat_activity where 1=1 and datname = \'python_test\' and datname != \'postgres\' and query like \'select drop_chunks%\';'
    value = statement.append(check_drop_chunk_statement)
    if value != NULL:
        return
    else:
        
        

'''
drop_chunks = 'select drop_chunks('hypertable[0][0]', interval '')'
SELECT drop_chunks( 'your_hypertable', interval '15 days');
'''