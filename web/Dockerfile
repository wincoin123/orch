FROM nginx

COPY requirements.txt .


RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN rm /etc/nginx/conf.d/default.conf
RUN pip3 install -r requirements.txt

WORKDIR /app/web/

CMD python3 blacklist.py
