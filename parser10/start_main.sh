cd /app

source /app/venv/bin/activate

python /app/main10.py &

echo $! > /app/main_pid10.txt
