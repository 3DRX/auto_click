from pynput.keyboard import Controller

import time

k = Controller()

if __name__ == "__main__":
    while True:
        print("Pressing W")
        k.press("W")
        time.sleep(5)
        k.release("W")
        print("Pressing S")
        k.press("S")
        time.sleep(5)
        k.release("S")
        pass
    pass
