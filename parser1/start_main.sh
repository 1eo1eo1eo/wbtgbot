cd /app

source /app/venv/bin/activate

python /app/main1.py &

echo $! > /app/main_pid1.txt
