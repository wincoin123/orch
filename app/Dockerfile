FROM nginx:alpine


RUN mkdir /app
COPY data /app
WORKDIR app

RUN apk update && apk add python3
RUN pip3 install -r requirements.txt
RUN rm /etc/nginx/conf.d/default.conf

CMD python3 mod_nc
