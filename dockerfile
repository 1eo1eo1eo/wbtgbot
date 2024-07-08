FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y default-mysql-client python3-pip \
    && playwright install && playwright install-deps

RUN chmod +x  parser1/start_main.sh parser1/stop_main.sh \
    parser2/start_main.sh parser2/stop_main.sh \
    parser3/start_main.sh parser3/stop_main.sh \
    parser4/start_main.sh parser4/stop_main.sh \
    parser5/start_main.sh parser5/stop_main.sh \
    parser6/start_main.sh parser6/stop_main.sh \
    parser7/start_main.sh parser7/stop_main.sh \
    parser8/start_main.sh parser8/stop_main.sh \
    parser9/start_main.sh parser9/stop_main.sh \
    parser10/start_main.sh parser10/stop_main.sh

    CMD ["sh", "-c", "sleep 10 && python3 run.py"]