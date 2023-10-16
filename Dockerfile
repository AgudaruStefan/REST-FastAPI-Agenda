FROM python:3.10-slim

WORKDIR /code

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /code
RUN poetry install
COPY ./app /code/app
COPY ./alembic /code/alembic 
COPY alembic.ini /code

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]


