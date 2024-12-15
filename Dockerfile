FROM python:3.12-alpine

WORKDIR /workdir
ENV PYTHONPATH=/workdir

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./alembic.ini .

COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
