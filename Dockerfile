FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirement.txt /requirement.txt
RUN pip install -r /requirement.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app
