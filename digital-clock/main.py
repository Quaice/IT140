# main.py

from display import Display
import datetime
import sys
import msvcrt

def main():
    ntime = datetime.datetime.now()
    delta = datetime.timedelta(seconds=1)

    while True:
        # b'\x1b'
        if msvcrt.kbhit():
            if msvcrt.getch() == b'\x1b':
                exit("User exited the program.")

        period = datetime.datetime.now()

        if period >= ntime:
            display.cls()
            time = datetime.datetime.now()
            time = time.strftime("%I:%M:%S")
            display.printdigits(time)
            ntime += delta

if __name__ == '__main__':
    style = sys.argv[1] if len(sys.argv) > 1 else 'block'
    display = Display(style)
    main()