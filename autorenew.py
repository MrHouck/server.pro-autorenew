import time
import pyautogui


while True:
    pyautogui.moveTo(150, 960, duration = 1) 
    pyautogui.click()

    pyautogui.moveTo(790, 620, duration=1)
    pyautogui.click()
    time.sleep(2400)
