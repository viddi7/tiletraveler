currentX=1
currentY=1
checker = 0

while True:
    #Hvert er hægt að fara
    if checker == 0:
        if currentX == 1 and currentY == 1:
            print("You can travel: (N)orth.")
        elif currentX == 1 and currentY == 2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif currentX == 1 and currentY == 3:
            print("You can travel: (E)ast or (S)outh.")
        elif currentX == 1 and currentY == 3:
            print("You can travel: (S)outh or (E)ast.")
        elif currentX == 2 and currentY == 1:
            print("You can travel: (N)orth")
        elif currentX == 2 and currentY == 2:
            print("You can travel: (S)outh or (W)est.")
        elif currentX == 2 and currentY == 3:
            print("You can travel: (E)ast or (W)est.")
        elif currentX == 3 and currentY == 1:
            print("Victory!")
            break
        elif currentX == 3 and currentY == 2:
            print("You can travel: (N)orth or (S)outh.")
        elif currentX == 3 and currentY == 3:
            print("You can travel: (S)outh or (W)est.")



    user_input = input("Direction: ")

    #Hvaða áttir þú getur farið
    if user_input == "n" or user_input == "N":
        if currentX == 1 and currentY == 3:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 3:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 3:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 2:
            print("Not a valid direction!")
            checker = 1
        else:
            currentY += 1
            checker = 0
    if user_input == "s" or user_input == "S":
        if currentX == 1 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 3:
            print("Not a valid direction!")
            checker = 1
        else:
            currentY -= 1
            checker = 0
    if user_input == "e" or user_input == "E":
        if currentX == 1 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 2:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 2:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 3:
            print("Not a valid direction!")
            checker = 1
        else:
            currentX += 1
            checker = 0
    if user_input == "w" or user_input == "W":
        if currentX == 1 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 1 and currentY == 2:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 1 and currentY == 3:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 2 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 1:
            print("Not a valid direction!")
            checker = 1
        elif currentX == 3 and currentY == 2:
            print("Not a valid direction!")
            checker = 1
        else:
            currentX -= 1
            checker = 0
    if user_input != "n" and user_input != "N" and user_input != "s" and user_input != "S" and user_input != "e" and user_input != "E" and user_input != "w" and user_input != "W":
        print("Not a valid direction!")
        checker = 1