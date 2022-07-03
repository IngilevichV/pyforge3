FROM python:3.9-slim-buster

WORKDIR /code

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]