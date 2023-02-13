import json
import requests

URL = "http://127.0.0.1:8000/create/"

data={
    'id': 5,
    'name':'Rahul',
    'roll':106,
    'city': 'Thane'
}

json_data=json.dumps(data)
r=requests.post(url= URL, data=json_data)
data=r.json()
print(data)

### for get request ####
# r=requests.get(url= URL)
# data=r.json()
# print(data)

























# a=[321,123,421,521,678]
# new=[]
#
# for i in a:
#     if i <600:
#         b=i//100
#         c=i%10
#         d=(b*10)+(c)
#         new.append(d)
#     else:
#         new.append(i)
#
# print(new)