#!/bin/python
import csv 
#import psycopg2

dict_list = []
print(dict_list)

with open ("vm_state_copy.out", 'r') as file:
    for row in file:
        line = row.strip()
        values = line.split(',')
        drop_stat_dict = {
             'chunk_stat': values[5]
        }
        dict_list.append(drop_stat_dict)
        
        
print(dict_list)