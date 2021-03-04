# start from base
FROM ubuntu:18.04
LABEL maintainer="Your Name <youremailaddress@provider.com>"
RUN apt-get update -y && apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "./main.py" ]

#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
#RUN apk --update add bash nano
#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static
#WORKDIR /usr/src/app
#COPY . .
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt