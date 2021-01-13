FROM python:3.8

RUN apt-get update -y

# RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential htop

# --------------------------------
# Server Code and Data

RUN mkdir /bits /bits/home /bits/airflow

WORKDIR /bits/

COPY xreq/requirements.txt /bits
RUN pip install -r /bits/requirements.txt

RUN useradd -M owner
RUN chown -R owner:owner /bits

USER owner

ENV AIRFLOW_HOME /bits/airflow
ENV HOME /bits/home

RUN airflow db init

