FROM python:3.11.0-alpine3.16

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

CMD ["python", "./main.py", "https://wikipedia.org"]

