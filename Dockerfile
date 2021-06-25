FROM continuumio/anaconda3

WORKDIR /app

COPY . /app

RUN pip install gunicorn

ENV FLASK_APP=server.py

EXPOSE 80

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:80", "-w", "4", "server:app"]