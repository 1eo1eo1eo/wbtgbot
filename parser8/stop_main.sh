if [ -f /app/mainfiles/main_pid8.txt ]; then
    PID=$(cat /app/mainfiles/main_pid8.txt)
    kill -9 $PID
    rm /app/mainfiles/main_pid8.txt
else
    echo "PID file not found"
fi
