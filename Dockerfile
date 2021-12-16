FROM python:latest
    
COPY WebApp myapp4

# UZUPELNIJ POLECENIA (patrz README aplikacji WebApp, nie używaj srodowiska wirtualnego)
WORKDIR /myapp4

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5000

RUN export FLASK_RUN_PORT=$FLASK_RUN_PORT
RUN export FLASK_APP=$FLASK_APP
RUN export FLASK_ENV=$FLASK_ENV

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run", "-h", "127.0.0.1", "-p", "5000"]
