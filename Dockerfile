FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["app.py"]