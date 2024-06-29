cd /app

source /app/venv/bin/activate

python /app/main4.py &

echo $! > /app/main_pid4.txt
