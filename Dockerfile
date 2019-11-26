FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install pycopg2

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# copy project
COPY ./movie_backend .

COPY ./requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

RUN rm requirements.txt

# run gunicorn
CMD gunicorn movie_backend.movie_backend.wsgi:application --bind 0.0.0.0:$PORT

