cd /app

source /app/venv/bin/activate

python /app/mainfiles/main10.py &

echo $! > /app/mainfiles/main_pid10.txt
