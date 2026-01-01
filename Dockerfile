FROM python:3.14-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --no-cache-dir poetry 
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8080
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]