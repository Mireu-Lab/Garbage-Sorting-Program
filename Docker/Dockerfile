FROM python:3

RUN mkdir app
WORKDIR app

COPY ../ .

RUN sh Install/install.sh

CMD ["python3 App/main.py"]