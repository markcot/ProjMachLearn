# Code adapted from https://runnable.com/docker/python/dockerize-your-flask-application &
# https://docs.docker.com/engine/install/ubuntu/ &
# https://stackoverflow.com/a/61564831 &
# https://stackoverflow.com/a/60184224

# base image
FROM ubuntu:20.04

MAINTAINER Mark Cotter <g00376335@gmit.ie>

# update python & pip
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential

# We only copy requirements.txt first
COPY . /app

# Set work directory
WORKDIR /app

# Install requirements
RUN pip3 install -r requirements.txt --default-timeout=1000 --no-cache-dir

# Set program start point
ENTRYPOINT [ "python3" ]

# Run server
CMD [ "web-service.py" ]