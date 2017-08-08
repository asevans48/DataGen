'''
This file contains all DAO objects.

All DAO objects must contain the following:
 - initialization function with database,username, and password as parameters in that order
 - absolutely no getter or setter for the connection variable
 - The methods create_schema, create_table, insert, and close as specified below.

Created on Aug 7, 2017

@author: aevans
'''

import psycopg2 as pg


class PostgreDAO:
    
    conn = None
        
    def __init__(self,database, username,password):
        self.conn = pg.connect(dbname = database, user = username, password = password )
    
    
    def create_schema(self,schema,drop_if_exists = False):
        curr = self.conn.cursor()
        
        if drop_if_exists is True: 
            curr.execute("DROP SCHEMA IF NOT EXISTS {}".format(schema))
        
        curr.execute("CREATE SCHEMA IF NOT EXISTS {}".format(schema))
        curr.close()
    
    def create_table(self,table, cols, drop_if_exists = False):
        curr = self.conn.cursor()
        col_str = ','.join([x['name']+' '+x['type'] for x in cols]) 
        if drop_if_exists is True:
            curr.execute("DROP TABLE IF EXISTS {}".format(table))
        
        curr.execute('CREATE TABLE IF NOT EXISTS {} VALUES({})'.format(table,col_str))    
        curr.close()
        
    def insert(self,table,data):
        curr = self.conn.cursor()
        keys = []
        vals = []
        for k,v in data.iteritems():
            keys.append(k)
            vals.append(v)
        curr_str = "INSERT INTO {} ({}) VALUES({})".format(table,','.join(keys),','.join(vals))    
        curr.close()
        
    def close(self):
        self.conn.close()
