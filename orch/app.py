from flask import Flask, render_template, request, jsonify, url_for
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    data = {}
    try:
        resp = requests.get('http://192.168.56.20:8081/getBlockedIps')
        res_json = resp.json()
        for x in res_json['blockedIps']:
            value = {}
            value['last_timestamp'] = x[1]
            value['entries_last_minute'] = 6
            data[x[0]] = value
        print(data)
    except ValueError:
        data = []
    return render_template("index.html", data=data)

@app.route('/data', methods=['POST', 'GET'])
def post_data_for_filtering():
  if request.method == 'POST':
    data = request.get_json()
    with open('dummy.json', 'w') as fp:
      fp.write(json.dumps(data))
    return "done"

  elif request.method == 'GET':
    with open("dummy.json") as fp:
      try:
        data = json.load(fp)
      except ValueError:
        data = []


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

    refined_data = {}
    print(blacklist)
    for key, value in blacklist.items():
        if value['entries_last_minute'] > 6:
            refined_data[key] = value

    with open('dummyRefined.json', 'w') as fp:
        fp.write(json.dumps(refined_data, indent=4))
    print(refined_data)

    for key,value in refined_data.items():
        print(key)
        print(value)
        res = requests.post('http://192.168.56.20:8081/blockIp',json={'ip':key,'timestamp':value['last_timestamp']})
        print(res.__dict__)

    resp = requests.get('http://192.168.56.20:8081/getBlockedIps')
    res_json = resp.json()
    blocked_ips = {}
    for x in res_json['blockedIps']:
        blocked_ips[x[0]] = x
    
    return jsonify(blocked_ips)


if __name__ == '__main__':
    app.run()
