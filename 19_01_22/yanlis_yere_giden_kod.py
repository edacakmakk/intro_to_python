import pyautogui
import time

time.sleep(5)

def mesaj():
    pyautogui.write("naber")  #The application that sends endless messages to the person we want on WhatsApp
    pyautogui.press('enter')  #I have funny and unforgettable memories :DD


while True:
    mesaj()
    time.sleep(0)
