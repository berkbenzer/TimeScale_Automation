connect python_test;
select who,vm, action, date_format(start_time,'%d-%m-%Y') as start_t, \
        date_format(end_time, '%d-%m-%Y') as end_t, \
        NULL AS chunk_stat \
        from python_test.launcher_history \
        where 1=1 \
        and vm in ('dwh-ps','dwh-ps2')\
        and action = 'stop' \
        and who != 'system'\
        group by who,vm, action,start_t,end_t \
        order by start_time desc;
