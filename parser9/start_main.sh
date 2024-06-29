cd /app

source /app/venv/bin/activate

python /app/main9.py &

echo $! > /app/main_pid9.txt
