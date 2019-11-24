FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install pycopg2

RUN apk update \
    && apk add --virtual build-deps gcc python-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# RUN python src/manage.py migrate

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn movie_backend.wsgi:application --bind 0.0.0.0:$PORT

