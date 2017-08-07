## DataGen

This tool creates fake data based on SQL scripts from specific database design tools or specified configuration options in addition to specified options. It is meant to make the task of fake data generation for test cases and software creation much simpler. Data generators are created that may be used to randomize data generation within acceptable parameters and persist data generation
rules. The tool is meant to help improve software quality by allowing developers and quality control specialists to focus on the data used in test.

The tool is in its infancy so is mainly a simmple aid at the mount. Data generation tools will grow as the tool evolves.

Currently DataGen:
 - Is meant for testers and devs
 - Supports PostgreSQL
 - Is Written in Python
 - Is new
 
DataGen should not be used for academic test cases where data needs to be a representative subset of a universe.

### Building Useful Test Cases

Test cases are important to development and quality control work. Typically, a test case tests the boundaries of a tool/aplication under test. 

Developers have been proven to be fairly competent in handling common usage cases but relatively mediocre at handling abberations. This is not to say that if
a password checker tries to avoid certain characters being hashed and inserted into a credentials table it should be added but that developers should utilize boundary tests and related data.

If a program handles data between 1 and 10 different than handling data over 10 and less than one, data should include 0,1,10, and 11.

Other examples of useful data includes handling abnormal cases such as SKUs that are not integers or non-english names 

 
### Example 

Data is generated from lists at using a randomized choice. 

DataGen may be used as follows:

```

from datgen.utils import *
from datagen.dao import PostgreDAO

opts = genOpts()
dao = new PostgreDAO('db','user','pass')
dict = pg_sql_file_to_dict('sql_file_path')
gen_data(dict,opts,dao)

```

The dictionary used to generate data does not need to come from a DDL dump. It may be specified as follows:

```
 {'table' : {'cols':[{'name' : 'col_name' : 'type' : 'varchar(512)'},....]}}
```

It is recommended that tables be generated from DDL directly as it is database specific and more extensive. PGModeler, Oracle Database Designer, and other tools are available to help generate DDL.

### Data Generation Options

Data generation configurations are mainly generated by the programmer at this point. A dictionary of tables, columns, and data is used at random:

```

def gen_list(range):
  for i in range:
  	yield i
  	
my_list = list(gen_list(range(0,10)))
json_data = {'table' : {'col_name' : {'choices' : my_list}}}  	

```
It is also possible to specify weights for the choices to be made, limiting the need for repeating code:

```
weights = [.2,.3,.5]
json_data = {'table' : {'col_name' : {'choices': my_list, 'weights': weights}}}
```
The size of the weights provided must equal the size of the list presented.

### Persisting Configuration

Since dictionaries are used to configure the tool, the configuration can persist after a program finishes.

To persist the data:

```
import json

my_list = genList(range(0,10))
json_data = {'table' : {'col' : {'choices' : my_list}}}

with('data.config','w') as fp:
	fp.write(json.dumps(json_data))

with('data.config','r') as fp:
	json_data = repr(fp.read())

```

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