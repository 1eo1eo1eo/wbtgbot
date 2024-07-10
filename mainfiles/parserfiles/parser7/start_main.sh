cd /app

source /app/venv/bin/activate

python /app/mainfiles/main7.py &

echo $! > /app/mainfiles/main_pid7.txt
