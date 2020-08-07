# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-buster

LABEL AUTHOR="Santhosh Thottingal <santhosh.thottingal@gmail.com>"

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip3 install -r requirements.txt
RUN python translate.py
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 translate:app
