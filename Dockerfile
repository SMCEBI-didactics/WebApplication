FROM python:latest
        
COPY WebApp myapp8

# UZUPELNIJ POLECENIA (patrz README aplikacji WebApp, nie używaj srodowiska wirtualnego)

RUN pip install -r myapp8/requirements.txt
ENV FLASK_RUN_HOST=localhost
ENV FLASK_RUN_PORT=5000
ENV FLASK_APP=myapp8/app.py
ENTRYPOINT [ "python", "-m", "flask", "run" ]
