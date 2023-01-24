FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /person_api_service

WORKDIR /person_api_service

COPY ./requirements.txt /person_api_service

# install requirements in docker container
RUN pip install -r requirements.txt

# copy directory into container
COPY . /person_api_service/

