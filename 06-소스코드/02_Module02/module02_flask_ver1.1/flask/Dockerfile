FROM python:3.8.11-buster

WORKDIR /app

ADD . /app

RUN apt-get update
RUN pip install flask
RUN pip install flask-restx
RUN pip install uwsgi
RUN pip install -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]