FROM python:3.6

RUN mkdir src
WORKDIR /src
COPY requirements.txt gunicorn_start ./

RUN pip install -r requirements.txt

COPY django ./django

CMD ["sh", "gunicorn_start"]

