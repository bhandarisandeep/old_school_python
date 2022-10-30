***
This Program prints the GUI based automation or strings set by the user
for the message or GUI service.
***

import pyautogui
import time
import random

random.seed(10)
time.sleep(4)

count = 0
while count<=50:
    pyautogui.typewrite("hello CRACK by CC " + str(count))
    pyautogui.press("enter")
    count = count + 1
    time.sleep(random.random() * 10)

    
***
PS: Don't use this Automater on Peanut.
***
