# syntax=docker/dockerfile:1
FROM python:3.9-alpine3.13
ENV PYTHONUNBUFFERED=1

WORKDIR /code
EXPOSE 8000

COPY requirements.txt /code/
COPY . /code/
COPY ./scripts /scripts

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r requirements.txt && \
    apk add jpeg-dev zlib-dev libjpeg && \
    /py/bin/pip install Pillow && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app
CMD [ "run.sh" ]
# RUN pip install -r requirements.txt


