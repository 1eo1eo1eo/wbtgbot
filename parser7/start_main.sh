cd /app

source /app/venv/bin/activate

python /app/main7.py &

echo $! > /app/main_pid7.txt
