FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip &&\
    apt-get install -y vim

RUN mkdir /WebProject
WORKDIR /WebProject

COPY ./requirements.txt /WebProject/requirements.txt

EXPOSE 8000

RUN pip3 install -r requirements.txt
