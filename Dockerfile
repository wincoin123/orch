FROM python:alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

CMD flask run -h 0.0.0.0 -p 8080
