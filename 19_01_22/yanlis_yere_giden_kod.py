import pyautogui
import time

time.sleep(5)

def mesaj():
    pyautogui.write("naber")
    pyautogui.press('enter')


while True:
    mesaj()
    time.sleep(0)