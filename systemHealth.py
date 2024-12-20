import psutil
import shutil
import datetime
import time
import base64

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
    #check CPU usage every half second for given time check
    for i in range(cpuTime*2):
        array.append(psutil.cpu_percent())
        time.sleep(.5)
    CPUpercent = sum(array) / len(array)

    return CPUpercent

def option256():
    var = "4qCAICAgICAgICAgICAgICAgICAgICDioIDioIDioIDioIDioIDioIDioIDioIDio4Dio4DioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOg4qO24qCb4qCb4qCb4qCb4qC34qO24qOk4qOA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjsOKgn+KggeKgiOKis+KhgOKigOKjoOKjtOKhv+Kgv+Kgm+KggeKggOKggOKggOKggOKggArioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDioZ7ioIHioIDioIDioIDioIDio7/io7/io7/ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qG+4qCA4qKA4qOg4qOk4qOE4qK44qO/4qO/4qO/4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKjvuKggeKggOKjvuKgi+KgiOKgueKjv+Kjv+Kjv+Kjv+Khh+KggOKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDioIDioIDioIDioIDioIDioIDiorjioY/ioIDioIDiorvioYbioIDioIDiornio7/io7/io7/ioYfioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK44qGH4qCA4qCA4qK44qGH4qCA4qCA4qCI4qO/4qO/4qO/4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKiuOKhh+KggOKggOKiuOKjh+KggOKggOKggOKjv+Kjv+Khv+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDioIDioIDioIDioIDioIDioIDiorjioYfioIDioIDiorjio7/ioIDioIDioqDio7/io7/ioYfioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC44qO34qCA4qCA4qCI4qO/4qCA4qKA4qO+4qO/4qO/4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKjv+KhgOKggOKggOKgu+KituKjv+Kjv+Kjv+Khh+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDioIDioIDioIDioIDioIDiooDio6Tiob7ioIPioIDioIDioIDioIjio7/io7/io7/ioIHioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qKg4qO24qOv4qOk4qOk4qOk4qOk4qG04qC24qC24qO84qO/4qO/4qO34qOk4qOA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgieKgieKgieKggeKggOKggOKggA=="
    var = var.encode('utf-8')
    var = base64.b64decode(var)
    var = var.decode('utf-8')
    print(var)

def getMemory():
    memory = (psutil.virtual_memory().available * 100) / (psutil.virtual_memory().total)
    return memory

def getDiskSpace():
    total, used, free = shutil.disk_usage("/")
    freeDisk = (free/total)*100
    return freeDisk

def check(cpuTime):
    #get necessary data
    CPU = getCPUusage(cpuTime)
    measumentePeriod = ""
    if cpuTime >= 60:
        measurementPeriod = str(cpuTime/60) + " min "
    else:
        measurementPeriod = str(cpuTime) + " sec "
    memory = getMemory()
    freeDisk = getDiskSpace(

    CPUHealth = True
    memoryHealth = True
    diskHealth = True
    #format data
    CPU = float("{:.2f}".format(CPU))
    memory = float("{:.2f}".format(100-memory))
    freeDisk = float("{:.2f}".format(100-freeDisk))
    
    #check health and print status
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
    #get necessary data
    CPU = getQuickCPUusage()
    memory = getMemory()
    freeDisk = getDiskSpace()

    #format data
    CPU = float("{:.2f}".format(CPU))
    memory = float("{:.2f}".format(100-memory))
    freeDisk = float("{:.2f}".format(freeDisk))
    
    #print data
    print("Current CPU usage " + str(CPU) + "%")
    print("Current RAM usage " + str(memory) + "%")
    print("Current free Disk " + str(freeDisk) + "%")

def main():
    print("Welcome!")
    cpuTime = 60
    while True:
        #main menu
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
        elif choice == 256:
            option256()

        elif choice == 0:
            exit()
        else:
            print("[ERROR] Invalid option selected, please choose option from provided menu")



if __name__ == "__main__":
    main()
