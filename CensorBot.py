def saycommand(msg):
    text = open("Censor.txt", "r")
    listo = [line.strip("\n") for line in text.readlines()]
    for i in listo:
        if i in msg:
            print("Nope")
            break

while True:
    saycommand(input("Enter Message -> "))
    



