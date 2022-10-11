FROM python:3.10

WORKDIR /app

ENV FLASK_APP=flaskr/app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python3", "-m" , "flask", "run"]