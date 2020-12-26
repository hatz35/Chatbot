import random
import time
import json
import glob
import os

#Adding time sleep
def getJson(name):
    with open(name, 'r') as f:
        return json.load(f)

def chatbotsays(name, msg):
    print(name + ": " + msg)

def usersays():
    return input("Enter Message -> ").lower()

#WORK HERE
def botprocessing(filename, reply):
    responses = getJson(filename)
    foundIt = False
    for i in responses["tags"]:
        for j in i["inputs"]:
            if reply == j.lower():
                foundIt = True
                chatbotsays(filename.strip("Script.json"), random.choice(i["outputs"]))
                return
    if foundIt == False:
        chatbotsays(filename.strip("Script.json"), "I don't understand what you are saying.")

def allwork(human = False, cat = False):
    quit_button = "q"
    back_button = "b"
    print(f"Chatbot is starting! Quit chatbot by replying {quit_button}, Go back to Menu by replying {back_button}")
    while True:
        reply = usersays()
        if reply == quit_button:
            quit_ear5()
            break
        elif reply == back_button:
            menu()
            break
        else:
            if human == True:
                filename = "HumanScript.json"
            elif cat == True:
                filename = "CatScript.json"
            botprocessing(filename, reply)
#ALL CODE ABOVE OLD asf


def listchar():
    #Make your characteres Json files there
    currentdir = os.path.abspath(os.getcwd())
    path = os.path.join(currentdir, "Characters")
    os.chdir(path)
    return glob.glob('*.json')

def pickchar():
    mycharacters = listchar()
    count = 1
    for i in mycharacters:
        print(f"\n\n[{count}] - {i.strip('.json')}")
        count += 1
    ind = input("Press the Index of the Character you would like to chat with"))
    #START FROM HERE
    #GET CHARACTER FROM INDEX

def quit():
    print("Sayonara")

def menu():
    for i in range(7):
        if i != 3:
            print("--------------")
        else:
            print("----[MENU]----")
    time.sleep(1)
    print("\n[A] Talk \n[B] Quit Ear5 \n\nPress A or B")
    time.sleep(1)
    useranswer = usersays()
    if useranswer == "a":
        pickchar()
    elif useranswer == "b":
        quit()

menu()
