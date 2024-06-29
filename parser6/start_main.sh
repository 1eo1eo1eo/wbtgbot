cd /app

source /app/venv/bin/activate

python /app/main6.py &

echo $! > /app/main_pid6.txt
