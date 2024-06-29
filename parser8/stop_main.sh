if [ -f /app/main_pid8.txt ]; then
    PID=$(cat /app/main_pid8.txt)
    kill -9 $PID
    rm /app/main_pid8.txt
else
    echo "PID file not found"
fi
