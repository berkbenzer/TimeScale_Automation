connect python_test;
select who,vm, action, date_format(start_time,'%d-%m-%Y') as start_t, \
        date_format(end_time, '%d-%m-%Y') as end_t, \
        NULL AS chunk_stat \
        from python_test.table_name \
        where 1=1 \
        and vm in ('proc_1','proc_2')\
        and action = 'stop' \
        and who != 'system'\
        group by who,vm, action,start_t,end_t \
        order by start_time desc;
