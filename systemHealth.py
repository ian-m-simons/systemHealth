import psutil
import shutil

def main():
    print(psutil.cpu_percent(), "% CPU usage")
    print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, "% available RAM")
    total, used, free = shutil.disk_usage("/")
    print((free / total) * 100, "% free disk Space")


if __name__ == "__main__":
    main()
