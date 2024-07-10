if [ -f /app/mainfiles/main_pid10.txt ]; then
    PID=$(cat /app/mainfiles/main_pid10.txt)
    kill -9 $PID
    rm /app/mainfiles/main_pid10.txt
else
    echo "PID file not found"
fi
