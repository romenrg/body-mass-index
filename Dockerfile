FROM python:3.7-alpine
COPY . /bmi
WORKDIR /bmi

ENTRYPOINT python3 -m bmi