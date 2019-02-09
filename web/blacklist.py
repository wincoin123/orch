import jinja2
import json
import time
import subprocess
import sys


ip_list = ['172.31.0.1']
server_ip = 'http://192.168.99.100:8080'
while True:
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "nginx.conf.jinja"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(ip_list=ip_list, server_ip=server_ip)
    print(outputText)
    fp = open('/etc/nginx/conf.d/custom.conf', 'w')
    fp.write(outputText)
    subprocess.run(["nginx", "-s", "reload"])
    time.sleep(60)
