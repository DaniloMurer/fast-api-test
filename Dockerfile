FROM python:3.8

RUN pip install fastapi uvicorn

EXPOSE 8000

COPY ./app /app

WORKDIR /app

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
