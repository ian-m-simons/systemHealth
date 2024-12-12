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
 
def getCPUusage():
    CPUpercent = psutil.cpu_percent(interval=5)
    CPUpercent = str(CPUpercent)
    return CPUpercent

def getMemory():
    memory = (psutil.virtual_memory().available * 100) / (psutil.virtual_memory().total)
    memory = str(memory)
    return memory

def getDiskSpace():
    total, used, free = shutil.disk_usage("/")
    freeDisk = str((free/total)*100)
    return freeDisk

def main():
    uptime = get_uptime()
    CPU = getCPUusage()
    memory = getMemory()
    freeDisk = getDiskSpace()

    print("current uptime: "+uptime)
    print(CPU + "% CPU usage")
    print(memory + "% memory available")
    print(freeDisk + "% free disk Space")


if __name__ == "__main__":
    main()
