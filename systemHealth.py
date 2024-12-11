import psutil

def main():
    print(psutil.cpu_percent())
    print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

if __name__ == "__main__":
    main()
