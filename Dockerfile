FROM python:alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt dev-requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt

COPY . /usr/src/app
