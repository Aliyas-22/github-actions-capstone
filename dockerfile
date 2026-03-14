FROM python:3.14-slim

WORKDIR /project

COPY . /project

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","app.api:app", "--host", "0.0.0.0", "--port", "8000"]