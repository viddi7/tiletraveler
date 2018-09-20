currentX = 1
currentY = 1
movere = 0
checker = 0
trvl = "You can travel: "

def notvalid():
    global checker
    print("Not a valid direction!")
    checker = 1

def wall(x1):
    global checker
    global movere
    if x1 == "s" or x1 == "S" or x1 == "e" or x1 == "E" or x1 == "w" or x1 == "W":
        if currentX == 1 and currentY == 1:
            notvalid()
            movere = 0
            return
        elif currentX == 2 and currentY == 1:
            notvalid()
            movere = 0
            return
        elif currentX == 3 and currentY == 1:
            notvalid()
            movere = 0
            return
    if x1 == "n" or x1 == "N" or x1 == "s" or x1 == "S":
        if currentX == 2 and currentY == 3:
            notvalid()
            movere = 0
            return
    if x1 == "n" or x1 == "N" or x1 == "e" or x1 == "E":
        if currentX == 3 and currentY == 3:
            notvalid()
            movere = 0
            return
        elif currentX == 2 and currentY == 2:
            notvalid()
            movere = 0
            return
    if x1 == "n" or x1 == "N" or x1 == "w" or x1 == "W":
        if currentX == 1 and currentY == 3:
            notvalid()
            movere = 0
            return
    if x1 == "e" or x1 == "E" or x1 == "w" or x1 == "W":
        if currentX == 3 and currentY == 2:
            notvalid()
            movere = 0
            return
    if x1 == "w" or x1 == "W":
        if currentX == 1 and currentY == 2:
            notvalid()
            movere = 0
            return
    else:
        movere = 1
    if x1 != "s" and x1 != "S" and x1 != "e" and x1 != "E" and x1 != "w" and x1 != "W" and x1 != "n" and x1 != "N":
        notvalid()
        return
    if x1 == "s" or x1 == "S" or x1 == "e" or x1 == "E" or x1 == "w" or x1 == "W" or x1 == "n" or x1 == "N":
        checker = 0
        
def mover():
    global currentY
    global currentX
    if user_input == "s" or user_input == "S":
        currentY-=1
    elif user_input == "n" or user_input == "N":
        currentY+=1
    elif user_input == "w" or user_input == "W":
        currentX-=1
    elif user_input == "e" or user_input == "E":
        currentX+=1

while True:
    if checker == 0:
        if currentX == 1 and currentY == 1:
            print(trvl+"(N)orth.")
        elif currentX == 1 and currentY == 2:
            print(trvl+"(N)orth or (E)ast or (S)outh.")
        elif currentX == 1 and currentY == 3:
            print(trvl+"(E)ast or (S)outh.")
        elif currentX == 1 and currentY == 3:
            print(trvl+"(S)outh or (E)ast.")
        elif currentX == 2 and currentY == 1:
            print(trvl+"(N)orth.")
        elif currentX == 2 and currentY == 2:
            print(trvl+"(S)outh or (W)est.")
        elif currentX == 2 and currentY == 3:
            print(trvl+"(E)ast or (W)est.")
        elif currentX == 3 and currentY == 1:
            print("Victory!")
            break
        elif currentX == 3 and currentY == 2:
            print(trvl+"(N)orth or (S)outh.")
        elif currentX == 3 and currentY == 3:
            print(trvl+"(S)outh or (W)est.")

    user_input = input("Direction: ")
    wall(user_input)
    if movere == 1:
        mover()