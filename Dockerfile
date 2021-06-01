FROM continuumio/anaconda3

WORKDIR /app

COPY . /app

RUN pip install gunicorn

ENV FLASK_APP=server.py

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "server:app"]