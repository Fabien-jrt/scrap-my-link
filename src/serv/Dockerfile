FROM python:3.11.0-alpine3.16

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./ .

EXPOSE 4444

CMD ["python", "main.py"]

