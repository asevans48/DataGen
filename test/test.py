'''
Created on Aug 7, 2017

@author: aevans
'''
from datagen.utils import *
from datagen.dao import PostgreDAO


#test data generators
def getNames():
    pass

def getStoreNames():
    return ['FashionSense','DeesBees1','DeesBees2','TopShelf','ProLook']




if __name__ == "__main__":
    dao = PostgreDAO('shopper_dev','postgres','rtp*4500')
    dicts = pgmodeler_sql_file_to_dict("/home/aevans/Documents/simplrinsites/db/shopper_dev.sql")
    print(dicts)
    
    opts ={
        'shopper.store' : {
            'cols' : {
                'name':{
                    'choice_gen' : getStoreNames 
                }
            },
            'size' : 100               
        }
    }
    