import sys
import re
import datetime
import time
import json
import math
logfile = "D:/test_log.txt"

file = open(logfile, "r")
ips = []
data = {}
strptime = datetime.datetime.strptime
for text in file.readlines():
    text = text.rstrip()
    found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
    match = text.partition('[')[-1].rpartition(']')[0]
    if found and match:
        s = match.split()
        d=time.mktime(datetime.datetime.strptime(s[0], "%d/%b/%Y:%H:%M:%S").timetuple())
        ips.append({'ipAddress': found[0], 'timestamp': math.ceil(d)})
        
print(ips)           

json_data = json.dumps(data)
print (json_data)
