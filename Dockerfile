FROM python:3.10

WORKDIR /app

COPY ./dist/flaskr-0.1.0-py3-none-any.whl .

RUN pip3 install flaskr-0.1.0-py3-none-any.whl

EXPOSE 5000

CMD ["gunicorn","-b","0.0.0.0:5000","-w","1","flaskr:create_app()"]