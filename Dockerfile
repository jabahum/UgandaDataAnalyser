FROM python:3.9-slim-buster

ADD . .

WORKDIR /

RUN pip3 --default-timeout=3000 install pandas


RUN pip3 --default-timeout=3000  install -r requirements.txt

ENV FLASK_ENV=development

ENV FLASK_APP=main.py

ENV SERVER_URL=https://mediator-api-staging.health.go.ug

CMD [ "python3", "run.py"]
