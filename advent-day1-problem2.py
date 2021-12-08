def findWindowIncreases(text_file):

    increaseCount = 0

    myPuzzleInput = open(text_file,"r")

    myNumbers = myPuzzleInput.readlines()

    for i in range(len(myNumbers)):

        myNumbers[i] = int(myNumbers[i])

    myWindowSums = []

    for i in range(1, len(myNumbers)-1):

        myWindowSums.append(myNumbers[i-1] + myNumbers[i] + myNumbers[i+1])

    windowSumsIncreases = 0

    for i in range(1, len(myWindowSums)):

        if myWindowSums[i]>myWindowSums[i-1]:

            windowSumsIncreases += 1

    print(f"{windowSumsIncreases} window sums were larger than previous window sums.")

findWindowIncreases("advent1input.txt")
