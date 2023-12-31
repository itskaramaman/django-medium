FROM python:3.10-alpine3.13

ENV PYTHONBUFFERED 1

COPY requirements.txt /tmp/requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000 

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]