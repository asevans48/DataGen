## DataGen

This tool creates fake data based on sql scripts and specified options. It is meant to make the task of fake data generation for test cases and software creation much simpler.

Currently DataGen:
 - Supports PostgreSQL
 - Is Written in Python
 - Is new
 
DataGen should not be used for academic test cases where data needs to be a representative subset of a universe.
 
### Example 

Simply import 

'''
from datgen.utils import *
from datagen.dao import PostgreDAO

opts = None # to be completed later
dao = new PostgreDAO('db','user','pass')
dict = pg_sql_file_to_dict('sql_file_path')
gen_data(dict,opts,dao)

'''

An example of options that will be specfied will follow shortly once a standard is laid out and implemented.

### License

Copyright 2017 Andrew Evans

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.