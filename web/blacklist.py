import jinja2
import json
import time
import subprocess
import sys
import requests


ip_list = []
server_ip = 'http://192.168.99.100:8080'
while True:
    data = requests.get('http://192.168.27.44:8081/getIpList')
    print(data)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "nginx.conf.jinja"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(ip_list=ip_list, server_ip=server_ip)
    fp = open('/etc/nginx/conf.d/custom.conf', 'w')
    fp.write(outputText)
    subprocess.run(["nginx", "-s", "reload"])
    time.sleep(60)
