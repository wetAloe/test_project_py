FROM python:3.12-alpine

WORKDIR /src

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

CMD ["python", "run.py"]
