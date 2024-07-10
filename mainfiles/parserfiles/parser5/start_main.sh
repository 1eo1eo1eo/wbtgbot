cd /app

source /app/venv/bin/activate

python /app/mainfiles/main5.py &

echo $! > /app/mainfiles/main_pid5.txt
