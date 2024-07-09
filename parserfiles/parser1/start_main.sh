cd /app

source /app/venv/bin/activate

python /app/mainfiles/main1.py &

echo $! > /app/mainfiles/main_pid1.txt
