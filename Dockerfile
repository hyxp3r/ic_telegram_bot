FROM python:3.11

RUN mkdir /ic_bot
WORKDIR /ic_bot
COPY . /ic_bot

RUN pip3 install poetry
ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry install --no-root
