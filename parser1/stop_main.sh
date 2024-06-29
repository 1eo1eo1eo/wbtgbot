if [ -f /app/main_pid1.txt ]; then
    PID=$(cat /app/main_pid1.txt)
    kill -9 $PID
    rm /app/main_pid1.txt
else
    echo "PID file not found"
fi
