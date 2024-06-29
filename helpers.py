import logging
import os
import psutil

def is_process_running(pid):
    if pid is None:
        logging.error("PID is None, cannot check if process is running.")
        return False
    try:
        process = psutil.Process(pid)
        status = process.status()
        logging.info(f"Checking process {pid}: status={status}")
        return process.is_running() and status in [psutil.STATUS_RUNNING, psutil.STATUS_SLEEPING]
    except psutil.NoSuchProcess:
        logging.warning(f"No such process with PID {pid}")
        return False
    except Exception as e:
        logging.error(f"Error checking if process is running: {e}")
        return False

def read_pid_from_file(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return int(file.read().strip())
        except ValueError:
            logging.error(f"Error reading PID from file: {file_path}")
            return None
    logging.error(f"PID file does not exist: {file_path}")
    return None

def correct_image_url(url):
    if url.startswith('//'):
        return 'https:' + url
    return url
