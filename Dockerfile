FROM python:3.9-alpine
WORKDIR /app
COPY ./API_server .
RUN pip install --no-cache-dir -r requirements.txt
