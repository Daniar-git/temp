#FROM python:3.7-slim-buster
#
#ENV PYTHONUNBUFFERED=1
#WORKDIR /code
#COPY requirements.txt /code/
#
#RUN apt-get update && \
#    apt-get install -y libpq-dev python3-dev build-essential
#
#RUN apt-get update && apt-get install apk-tools
#
#RUN pip install psycopg2-binary
#RUN pip install psycopg2
#
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev \
#
#RUN pip install -r requirements.txt
#
#COPY .. /code/

FROM python:3.7-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt /code/

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        musl-dev \
        libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc python3-dev musl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /code/
