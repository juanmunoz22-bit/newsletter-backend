FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV FLASK_APP=run.py

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]