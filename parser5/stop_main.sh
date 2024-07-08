if [ -f /app/mainfiles/main_pid5.txt ]; then
    PID=$(cat /app/mainfiles/main_pid5.txt)
    kill -9 $PID
    rm /app/mainfiles/main_pid5.txt
else
    echo "PID file not found"
fi
