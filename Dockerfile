# Code https://runnable.com/docker/python/dockerize-your-flask-application &
# https://docs.docker.com/engine/install/ubuntu/ &
# https://stackoverflow.com/a/61564831 &
# https://stackoverflow.com/a/60184224
FROM ubuntu:20.04

MAINTAINER Mark Cotter <g00376335@gmit.ie>

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential

# We copy just the requirements.txt first to leverage Docker cache
COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt --default-timeout=1000 --no-cache-dir

ENTRYPOINT [ "python3" ]

CMD [ "web-service.py" ]
