'''
Created on Aug 7, 2017

@author: aevans
'''


import psycopg2 as pg
import re
import random

'''
Random choice based on weights. The length of the weights array must equal the length of the data array.
The weights do not all need to be less than 1.0 or even sum to 1.0

@param data: The data to choose from
@param weights: The weights to use in picking the data. These should be doubles.
@return A randomized choice from the data array
'''
def random_weighted_choice(data,weights):
    assert(len(data) == len(weights))
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

@param sql_file_path:  The pat to the sql file generated from pgmodeler
@return: The list of dictionaries
'''
def pg_sql_file_to_dict(sql_file_path):
    sql = None
    with open(sql_file_path, 'r') as fp:
        sql = fp.read()
    pattern = re.compile("(?mis)CREATE\s+TABLE\s.*?[\-]+\s+ddl.end\s+[\-]+")
    matches = pattern.findall(sql)
    if matches is not None:
        for match in matches:
            pass
    
    
        
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