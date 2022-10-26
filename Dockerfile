FROM python:3.10-slim-bullseye

RUN pip install openai flask

WORKDIR /data/app
COPY app .

EXPOSE 1337

CMD ["python3", "/data/app/app.py"]