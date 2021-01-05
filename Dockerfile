# Code adapted from https://runnable.com/docker/python/dockerize-your-flask-application &
# https://docs.docker.com/engine/install/ubuntu/ &
# https://stackoverflow.com/a/61564831 &
# https://stackoverflow.com/a/60184224 &
# https://stackabuse.com/dockerizing-python-applications/ &
# https://gist.github.com/monkut/c4c07059444fd06f3f8661e13ccac619 &
# https://docs.docker.com/compose/gettingstarted/ 

# base linux image
FROM ubuntu:20.04

MAINTAINER Mark Cotter "g00376335@gmit.ie"

# update python & pip
RUN apt-get update && \
   apt-get install -y build-essential python3 python3-dev python3-pip && \
   # update pip
   python3 -m pip install pip --upgrade && \
   # install wheel for faster pip installations
   python3 -m pip install wheel

# Copy only requirements.txt first for update layer
COPY ./requirements.txt /app/requirements.txt

# Set working directory in container
WORKDIR /app

# Install python requirements with options to deal with intermitent connection issues
RUN pip3 install -r requirements.txt --default-timeout=1000

# Copy the remaining files
COPY . /app

# set flask server
ENV FLASK_APP=web-service.py

# Set flask container ip address
ENV FLASK_RUN_HOST=0.0.0.0

# Allow access to port 5000
EXPOSE 5000

# Program to run at start
ENTRYPOINT [ "flask" ]

# Run flask server
CMD [ "run" ]