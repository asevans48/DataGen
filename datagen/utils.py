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
def pgmodeler_sql_file_to_dict(sql_file_path):
    tables = []
    sql = None
    with open(sql_file_path, 'r') as fp:
        sql = fp.read()
   
    pattern = re.compile("(?mis)CREATE\s+TABLE\s.*?[\-]+\s+ddl.end\s+[\-]+")
    matches = pattern.findall(sql)
    if matches is not None:
        for match in matches:
            #pre tables
            txt = re.sub('(?mis)USING INDEX TABLESPACE.*|TABLESPACE.*|[\-]+\s+ddl.*','',match)
            
            #prepare columns
            table = None
            col_txt = None
            cols = None
            key_types = None
            tparts = re.search('(?mis)CREATE\s+TABLE\s+(.+?)?\((.+)',txt)
            if tparts is not None:
                table = tparts.group(1)
                col_txt = tparts.group(2)
            
            if table is not None and col_txt is not None:
                cols = col_txt.split(",")
                key_types = [re.split("\s+",x.strip())[:2] for x in cols if "PRIMARY KEY" not in x]
                cols = [{'name' : x[0], 'type' :  x[1]} for x in key_types if len(x) is 2]
                tables.append({table : {'cols' : cols}})
                
    return tables            
                
                
    
        
'''
Generate fake data using the list of dictionaries, supplied options, and a data acecss object

@param dict: The list of ditionaries to use
@param opts: The options to use
@param dao: The data access object
'''
def gen_data(dict, opts,dao):
    pass