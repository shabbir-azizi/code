from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput) / time_r
    return round(speed, 2)

while True:
    ck = input("Ready for typing test: Yes / No: ")
    if ck.lower() == "yes":
        test = [
            "A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long.",
            "My name is Shabbir Quetta.",
            "Welcome to WsCube Tech Jodhpur."
        ]
        test1 = r.choice(test)
        print("***** Typing Speed *****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()
        print('Speed:', speed_time(time_1, time_2, testinput), "w/sec")
        print("Errors:", mistake(test1, testinput))
    elif ck.lower() == 'no':
        print("Thank you for joining.")
        break
    else:
        print("Wrong input.")




