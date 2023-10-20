FROM python:3.10-slim
RUN apt-get update
RUN apt-get -y install gcc

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]