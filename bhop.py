import threading
from pynput.keyboard import Key, Listener, Controller
from time import sleep

presses = 0
keyboard = Controller()

def worker(num):
    if num == 0:
        def on_press(key):
            global presses
            
            if str(key) == "<269025153>":
                presses += 1

        def on_release(key):
            global presses

            if str(key) == "<269025153>":
                presses = 0

        # Collect events until released
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    else:
        while True:
            sleep(0.05)
            
            if presses > 0:
                keyboard.press(Key.space)
                keyboard.release(Key.space)


threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()