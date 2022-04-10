# syntax=docker/dockerfile:1
FROM python:3.10

# install client libs
RUN apt update -y && apt upgrade -y
RUN apt install -y python3-dev libpq-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
RUN mkdir -p /usr/src/app

# copy over setup files
COPY requirements.txt /usr/src/app
COPY entrypoint.sh /usr/src/app

# set working directory
WORKDIR /usr/src/app
RUN chmod +x *.sh

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy remaining files
COPY . /usr/src/app

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
