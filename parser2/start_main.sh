cd /app

source /app/venv/bin/activate

python /app/mainfiles/main2.py &

echo $! > /app/mainfiles/main_pid2.txt
