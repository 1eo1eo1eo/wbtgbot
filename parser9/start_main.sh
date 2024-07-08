cd /app

source /app/venv/bin/activate

python /app/mainfiles/main9.py &

echo $! > /app/mainfiles/main_pid9.txt
