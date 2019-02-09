import json
with open("dummy.json") as file:  
    data = json.loads(file.read())
blacklist = {}
          
for i in data:
    if i['ipAddress'] in blacklist:
        blacklist[i['ipAddress']]['entries_last_minute'] += 1
    else:
        blacklist[i['ipAddress']] = {}
        blacklist[i['ipAddress']]['entries_last_minute'] = 1
        blacklist[i['ipAddress']]['last_timestamp'] = i['timestamp']
        

    if blacklist[i['ipAddress']]['last_timestamp'] < i['timestamp']:
        blacklist[i['ipAddress']]['last_timestamp'] = i['timestamp']

print(json.dumps(blacklist, indent=4))
refined_data = {}

for key, value in blacklist.items():
    print(key, value)
    if value['entries_last_minute'] > 6:
        refined_data[key] = value

print(refined_data)

with open("dummyRefined.json", 'w') as file:
    file.write(json.dumps(refined_data, indent=4))


