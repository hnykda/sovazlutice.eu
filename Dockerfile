FROM python:3.6

COPY requirements.txt gunicorn_start ./

RUN pip install -r requirements.txt
CMD ["sh", "gunicorn_start"]

