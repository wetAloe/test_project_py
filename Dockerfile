FROM python:3.12-alpine

WORKDIR /workdir
ENV PYTHONPATH=/workdir

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "src/run.py"]
