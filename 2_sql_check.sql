'''  
    Check drop_chunk statement 
'''

check_drop_statment= 'select  datname,pid,usename,query,query_start from pg_stat_activity where 1=1 and datname = \'python_test\' and datname != \'postgres\' and query like \'select drop_chunks%\';'



'''  
    Check user sessions statement 
'''
select * from pg_stat_activity
where 1=1
and usename != 'postgres'
and datname != 'postgres'
;


'''
    terminate sessions except from Postgres user
'''

SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.usename <> 'postgres' 
AND pg_stat_activity.application_name <> 'pgAdmin';