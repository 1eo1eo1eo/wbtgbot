cd /app

source /app/venv/bin/activate

python /app/mainfiles/main8.py &

echo $! > /app/mainfiles/main_pid8.txt
