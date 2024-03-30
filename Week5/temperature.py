import time

maxtemperature = float(input("enter the max temperature in"))
substancetemperature = float(input("enter the substance's temperature in"))


while substancetemperature > maxtemperature:
    print("temperature is too high,please wait five minutes")
    print("turn down and wait")
    time.sleep(300)
    print("again and enter in")
    substancetemperature = float(input("enter the substance temperature in"))


