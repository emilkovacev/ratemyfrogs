FROM python:3.10
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
CMD uvicorn server:app --host="0.0.0.0" --port="5000"
