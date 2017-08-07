'''
This file contains all DAO objects.

All DAO objects must contain the following:
 - initialization function with database,username, and password as parameters in that order
 - absolutely no getter or setter for the connection variable
 - The methods create_schema, create_table, insert, and close as specifeid below.

Created on Aug 7, 2017

@author: aevans
'''

import psycopg2 as pg


class PostreDAO:
    
    conn = None
        
    def __init__(self,database, username,password):
        self.conn = pg.connect(dbname = database, user = username, password = password )
    
    
    def create_schema(self,schema,drop_if_exists = True):
        pass
    
    def create_table(self,table, drop_if_exists = True):
        pass
    
    def insert(self,json):
        pass
        
    def close(self):
        self.conn.close()
