#Task 3  Done
#      ***Trafic Light Simulation***

print("***Trafic Light Simulation***")
print("Enter light colour, done to finish")

import time
while True:
    light =input("Enter Light Colour:")

    if light == "green":
        (time.sleep(3))
        print("GO")
    elif light == "yellow":
        (time.sleep(2))
        print("Slow Down")
    elif light == "red":
        (time.sleep(5))
        print("Stop")
    if light == "done":
        break



     