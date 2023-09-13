from pynput.keyboard import Controller

import time

k = Controller()

if __name__ == "__main__":
    while True:
        print("Pressing W")
        k.press("W")
        time.sleep(2)
        k.release("W")
        print("Pressing S and W")
        k.press("S")
        k.press("W")
        time.sleep(2)
        k.release("S")
        k.release("W")
        pass
    pass
