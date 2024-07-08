cd /app

source /app/venv/bin/activate

python /app/mainfiles/main6.py &

echo $! > /app/mainfiles/main_pid6.txt
