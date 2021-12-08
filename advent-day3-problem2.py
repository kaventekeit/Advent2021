# Both the oxygen generator rating and the CO2 scrubber
# rating are values that can be found in your diagnostic
# report - finding them is the tricky part. Both values are
# located using a similar process that involves filtering
# out values until only one remains. Before searching for
# either rating value, start with the full list f binary
# numbers and CONSIDER JUST THE FIRST BIT of those numbers.
# Then:

# - Keep only numbers selected by the BIT CRITERIA for the
# type of rating value for which you are searching. Discard
# numbers which do not match the bit criteria.
# - If you only have one number left, stop; this is the
# rating value for which you are searching.
# - Otherwise, repeat the process, considering the next bit
# to the right.

# The bit criteria depends on which type of rating value
# you want to find:
# - To find the OXYGEN GENERATOR RATING, determine the
# MOST COMMON value in the current position, and keep only
# numbers with that bit in the position.
# If 0 and 1 are equally common, keep values with a 1.
# [ but they can't be - we saw that in the last problem, ]
# [ right? ]
# - To find the CO2 scrubber rating, determine the LEAST
# COMMON value [ 0 or 1 ] in the current bit position, and
# keep only numbers with that bit in that position.
# If 0 and 1 are equally common, keep values with a 0.

# Finally, to find the life support rating, multiply the oxygen
# generator rating by the CO2 scrubber rating to get the
# life support rating.

def getPowerConsumption(inputFile):

    puzzleInput = open(inputFile, "r")

    myCrypticNumbers = puzzleInput.readlines()

    O2List = []
    CO2List = []

    for i in myCrypticNumbers:
        O2List.append(i)
        CO2List.append(i)


    # HERE BEGINS THE O2 WINNOWING

    numIndex = 0
    bitIndex = 0

    while bitIndex in range(len(myCrypticNumbers[numIndex])):

        myO2OnesinColumnTally = 0
        while numIndex in range(len(O2List)):# possible
            if O2List[numIndex][bitIndex]=='1':
                myO2OnesinColumnTally += 1

            numIndex += 1

        myO2ZerosinColumnTally = len(O2List) - myO2OnesinColumnTally

        if myO2OnesinColumnTally>myO2ZerosinColumnTally:
            print(f'The most common bit in column {bitIndex} is 1.')

        else:
            print(f'The most common bit in colum {bitIndex} is 0.')

        numIndex = 0
        while numIndex in range(len(O2List)):
            if myO2OnesinColumnTally>=myO2ZerosinColumnTally: # THIS IS WHERE THE PROBLEM ISs
                myIndex = 0
                myListSize = len(O2List)
                while myIndex<myListSize and myListSize>=2:
                    if O2List[myIndex][bitIndex]=='0':
                        O2List.pop(myIndex)
                    else:
                        myIndex += 1

                    myListSize = len(O2List)


            else:
                myIndex = 0
                myListSize = len(O2List)
                while myIndex<myListSize and myListSize>=2:
                    if O2List[myIndex][bitIndex]=='1':
                        O2List.pop(myIndex)
                    else:
                        myIndex += 1

                    myListSize = len(O2List)

            numIndex += 1

        numIndex = 0

        bitIndex += 1



    # HERE BEGINS THE CO2 NARROWING

    numIndex = 0
    bitIndex = 0

    while bitIndex in range(len(myCrypticNumbers[numIndex])):

            myCO2OnesinColumnTally = 0
            while numIndex in range(len(CO2List)):# possible
                if CO2List[numIndex][bitIndex]=='1':
                    myCO2OnesinColumnTally += 1

                numIndex += 1

            myCO2ZerosinColumnTally = len(CO2List) - myCO2OnesinColumnTally

            if myCO2OnesinColumnTally>myCO2ZerosinColumnTally:
                print(f'The most common bit in column {bitIndex} is 1.')

            else:
                print(f'The most common bit in column {bitIndex} is 0.')

            numIndex = 0
            while numIndex in range(len(CO2List)):

                if myCO2OnesinColumnTally<myCO2ZerosinColumnTally:

                    myIndex = 0
                    myListSize = len(CO2List)
                    while myIndex<myListSize and myListSize>=2:
                        if CO2List[myIndex][bitIndex]=='0':
                            CO2List.pop(myIndex)
                        else:
                            myIndex += 1

                        myListSize = len(CO2List)

                else:

                    myIndex = 0
                    myListSize = len(CO2List)
                    while myIndex<myListSize and myListSize>=2:
                        if CO2List[myIndex][bitIndex]=='1':
                            CO2List.pop(myIndex)
                        else:
                            myIndex += 1

                        myListSize = len(CO2List)

                numIndex += 1

            numIndex = 0

            bitIndex += 1


    binO2 = O2List[0]
    finalO2 = 0
    powerOfTwo = 1
    for bit in range(len(binO2)-1, -1, -1):
        try:
            next = int(binO2[bit])
            finalO2 += powerOfTwo*next
            powerOfTwo = powerOfTwo*2
        except:
            pass

    binCO2 = CO2List[0]
    finalCO2 = 0
    powerOfTwo = 1
    for bit in range(len(binCO2)-1, -1, -1):
        try:
            next = int(binCO2[bit])
            finalCO2 += powerOfTwo*next
            powerOfTwo = powerOfTwo*2
        except:
            pass



    print(f"MY O2 GENERATOR RATING IS {O2List}, {finalO2} AND MY "
            f"CO2 SCRUBBER RATING IS {CO2List}, {finalCO2}.")

    powerConsumption = finalO2*finalCO2

    print(f"My power consumption is allegedly {powerConsumption}.")



getPowerConsumption("advent-day3-input1.txt")
