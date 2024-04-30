def main():
    prev = 0
    diceval = 0
    def most_roled(dice, prev, diceval):
        for i in dice:
            k.append(i)
        for word in range(len(k)):
            if k[word] in check:
                check[k[word]] += 1
            else:
                check[k[word]] = 1
        for numbers in check:
            current = check[numbers]
            if current > prev:
                prev = current
                diceval = numbers

    continuing = " "
    allD = 0
    allC = 0
    k = []
    checkD= {}
    checkC= {}
    check= {}
    prevD = 0
    prevC = 0
    dave_dice = []
    campbell_dice = []
    with open("Dave_Dice.txt", "r") as davids_files:
        for line in davids_files:
            dave_dice = line.split()
            dave_dice = [ int(x) for x in dave_dice ]

    with open("Campbell_Dice.txt", "r") as campbells_files:
        for line in campbells_files:
            campbell_dice = line.split()
            campbell_dice = [ int(x) for x in campbell_dice ]
    #loop the inputs
    while continuing:
    #davids inputs
        for rolls in range(5):
            dave_roll = input("david's roll: ")
    #calculator
            if dave_roll == "cal":
                cal = input("Please input all your dice rolls with a space inbetween: ")
                cal = cal.split()
                dave = 0
                for amount in range(len(cal)):
                    dave_roll = int(cal[amount])
    #add to set
            dave_dice.append(int(dave_roll))

    #campbells inputs
        for rolls in range(5):
            campbell_roll = input("campbell's roll: ")
    #calculator
            if campbell_roll == "cal":
                cal = input("Please input all your dice rolls with a space inbetween: ")
                cal = cal.split()
                cambell = 0
                for amount in range(len(cal)):
                    campbell_roll += int(cal[amount])
    #add to set
            campbell_dice.append(int(campbell_roll))
    #continue?
        continuing = input("continue?: ")

    #calculations
    #avargages
    avrageC = sum(campbell_dice) // len(campbell_dice)
    avrageD = sum(dave_dice) // len(dave_dice)
    print("Daves avarage roll:", avrageD)
    print("Campbells avarage roll:", avrageC)
    if avrageD > avrageC:
        print("David has a higher average with it being", round(avrageD - avrageC,2), "higher" )
    elif avrageD == avrageC:
        print("both dave and campbell have an average of",avrageC)
    else:
        print("campbell has a higher average with it being", round(avrageC - avrageD,2), "higher")
        
    #davids most rolled
    dice = dave_dice
<<<<<<< HEAD
    most_roled(dice)
=======
    most_roled(dice, prev, diceval)
    prevD = prev
    dicevalD = diceval
>>>>>>> 4f052e4c0f17d311d35360256b7148f9fac43a09
    k = []
    check = {}
    dice = campbell_dice
<<<<<<< HEAD
    most_roled(dice)
=======
    most_roled(dice, prev, diceval)
    prevC = prev
    dicevalC = diceval
>>>>>>> 4f052e4c0f17d311d35360256b7148f9fac43a09

    if prevD == 0 and prevC == 0:
        print("dave did not have a most rolled as it was tied and Campbell did not have a most rolled as it was tied")
    elif prevD == 0:
        print("dave did not have a most rolled as it was tied", "campbells mos rolled was:", dicevalC, "rolled",prevC, "Times")
    elif prevC == 0:
        print("daves most rolled is:",dicevalD, "and this was rolled", prevD, "times. Campbell did not have a most rolled as it was tied")
    else:
        print("daves most rolled is:",dicevalD, "and this was rolled", prevD, "times.and campbells was:", dicevalC, "rolled",prevC, "Times")
        
    open('Campbell_Dice.txt', 'w').close()
    open('Dave_Dice.txt', 'w').close()
    f = open("Dave_Dice.txt", "a")
    for roll in dave_dice:
        f.write (str(roll) + " ")
    f.close()
    f = open("Campbell_Dice.txt", "a")
    for roll in campbell_dice:
        f.write (str(roll) + " ")
    f.close()
if __name__ == "__main__":
    main()