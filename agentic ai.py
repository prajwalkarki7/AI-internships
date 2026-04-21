raw_json='{"name":"Prajwal Karki","age":21}'

import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

parased_dict=json.loads(raw_json)
user=User(name=parased_dict['name'], age=parased_dict['age'])

print(user.name)
print(user.age)