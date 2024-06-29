cd /app

source /app/venv/bin/activate

python /app/main2.py &

echo $! > /app/main_pid2.txt
