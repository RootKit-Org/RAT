# syntax=docker/dockerfile:1
FROM python:3.11-buster

ADD . .
ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /attacker

ENTRYPOINT [ "python", "main.py" ]