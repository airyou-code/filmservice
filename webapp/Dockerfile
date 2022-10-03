FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src ./src
COPY ./start.sh ./start.sh

RUN chmod 777 start.sh