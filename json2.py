#using dictionaries:
import json
input='''{
"name":"akshat",
"phone":{
"type":"intl",
"number":"+1 123 456 7890"
},
"email":{
"hide":"yes"
}
}'''
info=json.loads(input)
print('NAME...',info['name'])
print('phone no...',info["phone"]["number"])
print("is email hidden...",info["email"]['hide'])
