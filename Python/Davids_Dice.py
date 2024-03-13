dice = {}
continuing = " "
allD = 0
allC = 0
k = []
checkD= {}
checkC= {}
prevD = 0
prevC = 0
dave_dice = []
campbell_dice = []
for line in open("Dice.txt", "r"):

    dave_dice = line.split()
    [eval(i) for i in dave_dice]
    print(dave_dice)
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
for i in dave_dice:
    k.append(i)
for word in range(len(k)):
    if k[word] in checkD:
      checkD[k[word]] += 1
    else:
      checkD[k[word]] = 1
for numbers in checkD:
    current = checkD[numbers]
    if current > prevD:
        prevD = current
        dicevalD = numbers

#campbells most rolled
k = []
for i in campbell_dice:
    k.append(i)
for word in range(len(k)):
    if k[word] in checkC:
      checkC[k[word]] += 1
    else:
      checkC[k[word]] = 1
for numbers in checkC:
    current = checkC[numbers]
    if current > prevC:
        prevC = current
        dicevalC = numbers
print("daves most rolled is:",dicevalD, "and this was rolled", prevD, "times.and campbells was:", dicevalC, "rolled",prevC, "Times")
f = open("Dice.txt", "a")
for roll in dave_dice:
    f.write (str(roll) + " ")
f.write ("\n")
f.write (str(campbell_dice))
f.close()
