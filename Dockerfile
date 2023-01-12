FROM ubuntu:latest

RUN apt update 
RUN apt install python3 python3-pip -y

WORKDIR /root/

RUN mkdir aplikacja

COPY app.py aplikacja/
COPY requirements.txt aplikacja/
COPY WebApp aplikacja/

WORKDIR /root/aplikacja

RUN pip install -r requirements.txt  

RUN export FLASK_APP=app.py

CMD ["flask", "run"]
