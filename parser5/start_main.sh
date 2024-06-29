cd /app

source /app/venv/bin/activate

python /app/main5.py &

echo $! > /app/main_pid5.txt
