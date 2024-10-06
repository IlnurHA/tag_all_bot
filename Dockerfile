FROM python:3-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && apt-get install python3-pip libpq-dev python-dev -y \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove python3-pip -y \
    && apt-get clean


COPY . /app

CMD [ "python", "main.py" ]