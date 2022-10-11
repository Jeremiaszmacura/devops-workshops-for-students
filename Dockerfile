FROM python:3.10

WORKDIR /app

ENV FLASK_APP=flaskr/app.py

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run"]