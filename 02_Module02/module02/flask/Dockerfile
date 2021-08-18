FROM ubuntu:latest

WORKDIR /WAS

RUN apt-get update
RUN apt install -y python3.8 python3-pip python3.8-dev
RUN pip install flask
RUN pip install flask-restx
RUN pip install uwsgi

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]