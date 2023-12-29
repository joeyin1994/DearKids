import time
import subprocess
from pyfiglet import figlet_format
from termcolor import colored


def main():
    input("Enter the author's name: ")
    p = subprocess.Popen(["genact", "-m", "simcity", "--speed-factor", "20"])
    start = time.time()
    while True:
        if time.time() > start + 5:
            p.kill()
            break
        time.sleep(5)
    print("\n")
    print((colored(figlet_format("Setup complete"), color="blue")))


if __name__ == '__main__':
    main()
