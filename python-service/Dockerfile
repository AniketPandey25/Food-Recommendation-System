FROM python:3.8-slim-buster

EXPOSE 5000

# Tell Python to not generate .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

ADD . /app