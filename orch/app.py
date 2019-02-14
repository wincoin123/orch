from flask import Flask, render_template, request, jsonify, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("dummyRefined.json") as fp:
      try:
        data = json.load(fp)
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

    for key, value in blacklist.items():
        if value['entries_last_minute'] > 6:
            refined_data[key] = value

    with open('dummyRefined.json', 'w') as fp:
        fp.write(json.dumps(refined_data, indent=4))

    return jsonify(refined_data)


if __name__ == '__main__':
    app.run()
