FROM python:3.10

WORKDIR /app

ENV FLASK_APP=flaskr/app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY ./dist/flaskr-0.1.0-py3-none-any.whl .

RUN pip3 install flaskr-0.1.0-py3-none-any.whl

EXPOSE 5000

COPY . .

CMD [ "python3", "-m" , "flask", "run"]