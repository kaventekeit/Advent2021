# Each bit in the gamma rate can be determined
# by finding the MOST COMMON BIT in the correpsonding
# position of all numbers in the diagnostic report.

# The epsilon rate is calculated in a similar way,
# but it's the least common bit.

# Multiply the gamma rate and the epsilon rate together
# to get the power consumption.

# Return the power consumption.

def getPowerConsumption(inputFile):

    puzzleInput = open(inputFile, "r")

    myCrypticNumbers = puzzleInput.readlines()

    bitsAtPosDict = {}

    for num in myCrypticNumbers:

        # these are gonna be STRINGS but we want that so we
        # can index into them

        myPos = 0

        for bit in num:

            if not (myPos in bitsAtPosDict):
                try:
                    bitsAtPosDict[myPos] = [int(bit)]
                except:
                    pass
            else:
                try:
                    bitsAtPosDict[myPos].append(int(bit))
                except:
                    pass

            myPos += 1

    gammaRateStr = ""
    epsilonRateStr = ""

    for key in bitsAtPosDict:

        zerosCount = 0
        onesCount = 0

        for bit in bitsAtPosDict[key]:

            if bit==0:
                zerosCount += 1
            elif bit==1:
                onesCount += 1

        if zerosCount>onesCount:
            gammaRateStr += '0'
            epsilonRateStr += '1'

        elif onesCount>zerosCount:
            gammaRateStr += '1'
            epsilonRateStr += '0'

    gammaRate = 0
    epsilonRate = 0

    powerOfTwo = 1

    for i in range(len(gammaRateStr)-1, -1, -1):

        gammaRate += int(gammaRateStr[i])*powerOfTwo

        powerOfTwo = powerOfTwo*2

    powerOfTwo = 1

    for j in range(len(epsilonRateStr)-1, -1, -1):

        epsilonRate += int(epsilonRateStr[j])*powerOfTwo

        powerOfTwo = powerOfTwo*2

    print(f"The epsilon rate is {epsilonRate} and "
            f"the gamma rate is {gammaRate}.")

    powerConsumption = epsilonRate*gammaRate

    print(f"The power consumption is {powerConsumption}.")

getPowerConsumption("advent-day3-input1.txt")
