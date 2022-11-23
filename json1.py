#using list:
import json
input='''[
{"id":"001",
"x":"2",
"name":"akshat"
},
{
"id":"007",
"x":"4",
"name":"daruka"
}
]'''
info=json.loads(input)
print("USER COUNT...",len(info))
for items in info:
    print("name:",items["name"])
    print("id:",items['id'])
    print("attribute",items['x'])
