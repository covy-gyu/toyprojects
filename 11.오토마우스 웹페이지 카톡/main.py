import pyautogui as p
import pyperclip
import time
import threading
import os

# print("Current working directory:", os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def send_message():
    threading.Timer(10, send_message).start()

    picPos = p.locateOnScreen("pic1.png")
    print(picPos)

    if picPos is None:
        picPos = p.locateOnScreen("pic2.png")
        print(picPos)

    if picPos is None:
        picPos = p.locateOnScreen("pic3.png")
        print(picPos)

    clickPos = p.center(picPos)
    p.doubleClick(clickPos)

    pyperclip.copy("자동 메시지")
    p.hotkey("ctrl", "v")
    time.sleep(1.0)

    p.write(["enter"])
    time.sleep(1.0)

    p.write(["escape"])
    time.sleep(1.0)


send_message()
