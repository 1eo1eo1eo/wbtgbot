cd /app

source /app/venv/bin/activate

python /app/mainfiles/main3.py &

echo $! > /app/mainfiles/main_pid3.txt
