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