cd /app

source /app/venv/bin/activate

python /app/main8.py &

echo $! > /app/main_pid8.txt
