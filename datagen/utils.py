'''
Created on Aug 7, 2017

@author: aevans
'''


import psycopg2 as pg
import re
import random

def random_weighted_choice(data,weights):
    total = sum(weights)
    d = random.uniform(0,total)
    sum = 0
    idx = 0
    while sum < d:
        sum += weights[idx]
        idx += 1
    return data[idx]    

'''
Convert PostgreSQL .sql files to a list of dictionaries.

@param sql_file_path:  The pat to the sql file 
@return: The list of dictionaries
'''
def pg_sql_file_to_dict(sql_file_path):
    sql = None
    with open(sql_file_path, 'r') as fp:
        sql = fp.read()
    match_list = re.match("(?mis)CREATE\s+(?=TABLE)", sql)
    
        
'''
Generate fake data using the list of dictionaries, supplied options, and a data acecss object

@param dict: The list of ditionaries to use
@param opts: The options to use
@param dao: The data access object
'''
def gen_data(dict, opts,dao):
    pass


if __name__ == "__main__":
    pass