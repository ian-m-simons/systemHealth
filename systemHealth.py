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
    array = []
    for i in range(120):
        array.append(psutil.cpu_percent())
        time.sleep(.5)
    CPUpercent = sum(array) / len(array)

    return CPUpercent

def getMemory():
    memory = (psutil.virtual_memory().available * 100) / (psutil.virtual_memory().total)
    return memory

def getDiskSpace():
    total, used, free = shutil.disk_usage("/")
    freeDisk = (free/total)*100
    return freeDisk

def main():
    
    while True:
        uptime = get_uptime()
        CPU = getCPUusage()
        memory = getMemory()
        freeDisk = getDiskSpace()
        CPUHealth = True
        memoryHealth = True
        diskHealth = True
        if CPU > 50:
            print("\a[WARNING] sustained higher CPU usage\nCPU has averaged " + str(CPU) + "% for 5 minutes")
            CPUHealth = False
        if memory < 10:
            print("\a[WARNING] RAM usage is at " + str(100-memory) + "%")
            memoryHealth = False
        if freeDisk < 10:
            print("\a[WARNING] Disk almost full, only " + str(freeDisk) + "% remaning")
            diskHealth = False
        if CPUHealth and memoryHealth and diskHealth:
            print("system is healthy")
        time.sleep(5)



if __name__ == "__main__":
    main()
