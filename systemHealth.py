import psutil
import shutil
import datetime
import time

def inputInt(prompt):
    success = False
    while not success:
        value = input(prompt)
        try:
            value = int(value)
            success = True
        except:
            print("[ERROR] Input must be integer")
    return value

def get_uptime():
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = int(now - boot_time)
    uptime_formatted = str(datetime.timedelta(seconds=uptime_seconds))
    return uptime_formatted

def getQuickCPUusage():
    return psutil.cpu_percent()

def getCPUusage(cpuTime):
    array = []

    for i in range(cpuTime*2):
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

def check(cpuTime):
    CPU = getCPUusage(cpuTime)
    measumentePeriod = ""
    if cpuTime >= 60:
        measurementPeriod = str(cpuTime/60) + " min "
    else:
        measurementPeriod = str(cpuTime) + " sec "
    memory = getMemory()
    freeDisk = getDiskSpace()
    CPUHealth = True
    memoryHealth = True
    diskHealth = True
    CPU = float("{:.2f}".format(CPU))
    memory = float("{:.2f}".format(100-memory))
    freeDisk = float("{:.2f}".format(100-freeDisk))
    
    if CPU > 50:
        print("\a[WARNING] sustained higher CPU usage\nCPU has averaged " + str(CPU) + "% for 5 minutes")
        CPUHealth = False
    if memory > 90:
        print("\a[WARNING] RAM usage is at " + str(10-memory) + "%")
        memoryHealth = False
    if freeDisk > 90:
        print("\a[WARNING] Disk almost full, only " + str(freeDisk) + "% remaning")
        diskHealth = False
    if CPUHealth and memoryHealth and diskHealth:
        print("\nsystem is healthy")
        print("CPU "+ measurementPeriod + "avg " + str(CPU) + "%")
        print("RAM usage " + str(memory) + "%")
        print("Disk usage " + str(freeDisk) + "%")

def Snapshot():
    CPU = getQuickCPUusage()
    memory = getMemory()
    freeDisk = getDiskSpace()
    CPU = float("{:.2f}".format(CPU))
    memory = float("{:.2f}".format(100-memory))
    freeDisk = float("{:.2f}".format(freeDisk))
    print("Current CPU usage " + str(CPU) + "%")
    print("Current RAM usage " + str(memory) + "%")
    print("Current free Disk " + str(freeDisk) + "%")

def main():
    print("Welcome!")
    cpuTime = 60
    while True:
        print("\n\nSystem Health Check, please select option below")
        print("1. continuous monitoring")
        print("2. quick monitor (single monitor cycle)")
        print("3. snapshot (view resources at this exact moment)")
        print("4. change how long to monitor length of monitor cycle (default 60 seconds)")
        print("0. exit")
        choice = inputInt("option: ")
        
        if choice == 1:
            while True:
                check(cpuTime)
                time.sleep(5)
        elif choice == 2:
            check()
        elif choice == 3:
            Snapshot()
        elif choice == 4:
            cpuTime = inputInt("please enter the number of seconds to use for monitor cycle ")
            while cpuTime < 1:
                print("[ERROR] time must be a positive number")
                cpuTime = inputInt("please enter the number of seconds to use for monitor cycle ")

        elif choice == 0:
            exit()
        else:
            print("[ERROR] Invalid option selected, please choose option from provided menu")



if __name__ == "__main__":
    main()
