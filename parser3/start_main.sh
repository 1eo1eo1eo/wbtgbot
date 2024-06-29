cd /app

source /app/venv/bin/activate

python /app/main3.py &

echo $! > /app/main_pid3.txt
