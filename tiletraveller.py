currentX=1
currentY=1

while True:
    #Hvert er hægt að fara m
    if currentX == 1 and currentY == 1:
        print("You can go North")
    elif currentX == 1 and currentY == 2:
        print("You can go North, South, East")
    elif currentX == 1 and currentY == 3:
        print("You can go South or East")
    elif currentX == 1 and currentY == 3:
        print("You can go South or East")
    elif currentX == 2 and currentY == 1:
        print("You can go North")
    elif currentX == 2 and currentY == 2:
        print("You can go South or West")
    elif currentX == 2 and currentY == 3:
        print("You can go East or West")
    elif currentX == 3 and currentY == 1:
        print("Victory!")
        break
    elif currentX == 3 and currentY == 2:
        print("You can go North or South")
    elif currentX == 3 and currentY == 3:
        print("You can go South or West")



    user_input = input("Direction: ")

    #Hvaða áttir þú getur farið
    if user_input == "n" or user_input == "N":
        if currentX == 1 and currentY == 3:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 3:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 3:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 2:
            print("Not a valid direction!")
        else:
            currentY += 1
    if user_input == "s" or user_input == "S":
        if currentX == 1 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 3:
            print("Not a valid direction!")
        else:
            currentY -= 1
    if user_input == "e" or user_input == "E":
        if currentX == 1 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 2:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 2:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 3:
            print("Not a valid direction!")
        else:
            currentX += 1
    if user_input == "w" or user_input == "W":
        if currentX == 1 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 1 and currentY == 2:
            print("Not a valid direction!")
        elif currentX == 1 and currentY == 3:
            print("Not a valid direction!")
        elif currentX == 2 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 1:
            print("Not a valid direction!")
        elif currentX == 3 and currentY == 2:
            print("Not a valid direction!")
        else:
            currentX -= 1
    if user_input != "n" and user_input != "N" and user_input != "s" and user_input != "S" and user_input != "e" and user_input != "E" and user_input != "w" and user_input != "W":
        print("Not a valid direction!")