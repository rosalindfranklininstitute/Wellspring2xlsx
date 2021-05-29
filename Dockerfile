FROM continuumio/anaconda3

WORKDIR /app

COPY . /app

ENV FLASK_APP=server.py

CMD [ "flask", "run" ]