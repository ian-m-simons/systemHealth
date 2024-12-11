import psutil
import shutil
import datetime
import time

def get_uptime():
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = int(now - boot_time)
    uptime_formatted = str(datetime.timedelta(seconds=uptime_seconds))
    return uptime_formatted

def main():
    uptime = get_uptime()
    print("current uptime: "+uptime)
    print(psutil.cpu_percent(), "% CPU usage")
    print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, "% memory available")
    total, used, free = shutil.disk_usage("/")
    print((free / total) * 100, "% free disk Space")


if __name__ == "__main__":
    main()
