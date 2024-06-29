if [ -f /app/main_pid9.txt ]; then
    PID=$(cat /app/main_pid9.txt)
    kill -9 $PID
    rm /app/main_pid9.txt
else
    echo "PID file not found"
fi
