FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y default-mysql-client python3-pip \
    && playwright install && playwright install-deps

RUN chmod +x  mainfiles/parserfiles/parser1/start_main.sh mainfiles/parserfiles/parser1/stop_main.sh \
    mainfiles/parserfiles/parser2/start_main.sh mainfiles/parserfiles/parser2/stop_main.sh \
    mainfiles/parserfiles/parser3/start_main.sh mainfiles/parserfiles/parser3/stop_main.sh \
    mainfiles/parserfiles/parser4/start_main.sh mainfiles/parserfiles/parser4/stop_main.sh \
    mainfiles/parserfiles/parser5/start_main.sh mainfiles/parserfiles/parser5/stop_main.sh \
    mainfiles/parserfiles/parser6/start_main.sh mainfiles/parserfiles/parser6/stop_main.sh \
    mainfiles/parserfiles/parser7/start_main.sh mainfiles/parserfiles/parser7/stop_main.sh \
    mainfiles/parserfiles/parser8/start_main.sh mainfiles/parserfiles/parser8/stop_main.sh \
    mainfiles/parserfiles/parser9/start_main.sh mainfiles/parserfiles/parser9/stop_main.sh \
    mainfiles/parserfiles/parser10/start_main.sh mainfiles/parserfiles/parser10/stop_main.sh

    CMD ["sh", "-c", "sleep 20 && python3 run.py"]